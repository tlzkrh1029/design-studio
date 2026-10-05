#!/usr/bin/env python3
"""Build the GEO block (water, roads, bridges, district boundaries) for the location-map pattern.

The output is the `const GEO = ...` object that reference.html draws. Coordinates are
integer metres around a centre point: x grows to the east, y grows to the south (screen
direction), so the page only has to scale and shift them.

Inputs
  --city       data/seoul.json from https://github.com/taekie/seoul-3d
               (OpenFreeMap z14 tiles in the OpenMapTiles schema, 2026-08-30 snapshot,
               (c) OpenStreetMap contributors, ODbL).
  --districts  kostat/2013/json/seoul_municipalities_geo_simple.json from
               https://github.com/southkorea/seoul-maps (KOSTAT 2013 census boundaries,
               repository licensed Apache-2.0).

Output shape
  {"river": [poly], "lakes": [poly, ...],
   "roads": {"<width class>": [line, ...], ...},
   "districts": [{"n": name, "p": [poly, ...]}, ...],
   "bridges": [{"n": name, "p": [line, ...]}, ...]}
  poly = [outer ring, hole, ...]; ring and line = [[x, y], ...]

Example: the map of the Lotte Konkuk Star City store (2026-10-05). --klat 37.527 keeps the
same east-west scale as the store coordinates already used on that page.
  python3 build_geo.py --city seoul-3d/data/seoul.json \\
    --districts seoul_municipalities_geo_simple.json \\
    --center 127.0702,37.5386 --klat 37.527 \\
    --bbox 126.975,37.488,127.152,37.566 \\
    --bridge 성수대교=127.0350,37.5364 --bridge 영동대교=127.0571,37.5300 \\
    --bridge 청담대교=127.0644,37.5265 --bridge 잠실대교=127.0920,37.5239 \\
    --bridge 천호대교=127.1111,37.5433 \\
    --out geo.json

Requires shapely 2.x (pip install shapely).
"""
import argparse
import json
import math

from shapely.geometry import LineString, Point, Polygon, box, shape
from shapely.ops import linemerge, transform, unary_union


def parts(g):
    return list(getattr(g, "geoms", [g]))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--city", required=True, help="seoul-3d style city JSON")
    ap.add_argument("--districts", required=True, help="district boundaries as GeoJSON")
    ap.add_argument("--center", required=True, help="lon,lat of the reference point")
    ap.add_argument("--bbox", required=True, help="lon_min,lat_min,lon_max,lat_max to keep")
    ap.add_argument("--klat", type=float, default=None,
                    help="latitude for the east-west metre scale (default: centre latitude)")
    ap.add_argument("--bridge", action="append", default=[],
                    help="name=lon,lat of a bridge to keep as its own layer; repeat as needed")
    ap.add_argument("--min-water-m2", type=float, default=15000, help="drop smaller water bodies")
    ap.add_argument("--min-road-width", type=float, default=2, help="drop narrower road classes")
    ap.add_argument("--tol-river", type=float, default=7, help="simplification tolerance (m)")
    ap.add_argument("--tol-lake", type=float, default=5)
    ap.add_argument("--tol-road", type=float, default=9)
    ap.add_argument("--tol-district", type=float, default=12)
    ap.add_argument("--min-road-len", type=float, default=120, help="drop shorter merged roads (m)")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    lon_c, lat_c = map(float, a.center.split(","))
    bb_ll = tuple(map(float, a.bbox.split(",")))
    klat = a.klat if a.klat is not None else lat_c
    KX = 111320 * math.cos(math.radians(klat))  # metres per degree of longitude
    KY = 110990                                   # metres per degree of latitude

    def to_m(x, y, z=None):
        return ((x - lon_c) * KX, (lat_c - y) * KY)

    def ints(coords):
        return [[round(x), round(y)] for x, y in coords]

    def enc_poly(g):
        return [ints(g.exterior.coords)] + [ints(h.coords) for h in g.interiors]

    # seoul-3d stores Web Mercator tile coordinates scaled to metres around meta.center
    city = json.load(open(a.city, encoding="utf-8"))
    meta = city["meta"]
    lon0, lat0 = meta["center"]
    kx, Z = meta["kx"], meta["z"]
    n = 2 ** Z
    cx = (lon0 + 180) / 360 * n
    cy = (1 - math.log(math.tan(math.radians(lat0)) + 1 / math.cos(math.radians(lat0))) / math.pi) / 2 * n

    def inv(wx, wy):
        tx = wx / kx * n + cx
        ty = -wy / kx * n + cy
        lon = tx / n * 360 - 180
        lat = math.degrees(math.atan(math.sinh(math.pi - 2 * math.pi * ty / n)))
        return lon, lat

    bb = box(*bb_ll)

    # water: union of all water polygons inside the box; the largest part is the river
    polys = []
    for poly in city["water"]:
        rings = [[inv(r[i], r[i + 1]) for i in range(0, len(r), 2)] for r in poly]
        if len(rings[0]) < 4:
            continue
        try:
            pg = Polygon(rings[0], [h for h in rings[1:] if len(h) >= 4])
            if not pg.is_valid:
                pg = pg.buffer(0)
        except Exception:
            continue
        if pg.intersects(bb):
            polys.append(pg)
    water = unary_union(polys).intersection(bb)
    water_ll = [g for g in parts(water) if g.area * KX * KY > a.min_water_m2]
    river_ll = max(water_ll, key=lambda g: g.area)

    # roads by width class, clipped to the box (rail excluded)
    roads_ll = {}
    for r in city["roads"]:
        if r.get("rail") or r["w"] < a.min_road_width:
            continue
        p = r["p"]
        ln = LineString([inv(p[i], p[i + 1]) for i in range(0, len(p), 2)])
        if not ln.intersects(bb):
            continue
        g = ln.intersection(bb)
        if g.geom_type == "LineString" and len(g.coords) >= 2:
            roads_ll.setdefault(str(r["w"]), []).append(g)

    out = {}
    water_m = [transform(to_m, g) for g in water_ll]
    river_m = transform(to_m, river_ll)
    rs = river_m.simplify(a.tol_river, preserve_topology=True)
    out["river"] = [enc_poly(g) for g in parts(rs)]
    out["lakes"] = [enc_poly(g.simplify(a.tol_lake, preserve_topology=True))
                    for g, src in zip(water_m, water_ll) if src is not river_ll]

    out["roads"] = {}
    for w, lines in roads_ll.items():
        merged = linemerge(unary_union([transform(to_m, l) for l in lines]))
        keep = []
        for g in parts(merged):
            if g.length < a.min_road_len:
                continue
            keep.append(ints(g.simplify(a.tol_road, preserve_topology=False).coords))
        out["roads"][w] = keep

    bbm = box(*to_m(bb_ll[0], bb_ll[3]), *to_m(bb_ll[2], bb_ll[1]))
    out["districts"] = []
    for f in json.load(open(a.districts, encoding="utf-8"))["features"]:
        g = transform(to_m, shape(f["geometry"]))
        if not g.intersects(bbm):
            continue
        g = g.simplify(a.tol_district, preserve_topology=True)
        out["districts"].append({"n": f["properties"]["name"], "p": [enc_poly(pp) for pp in parts(g)]})

    # bridges: road pieces over the river near each named point (longest first, up to 4)
    out["bridges"] = []
    for spec in a.bridge:
        name, ll = spec.split("=")
        tp = Point(*map(float, ll.split(",")))
        pieces = []
        for lines in roads_ll.values():
            for l in lines:
                if l.distance(tp) > 0.004:
                    continue
                for g in parts(l.intersection(river_ll)):
                    if g.geom_type == "LineString" and g.length > 0.0015 and g.distance(tp) < 0.003:
                        pieces.append(g)
        pieces.sort(key=lambda g: -g.length)
        if not pieces:
            print("warning: no river crossing found near", name)
            continue
        out["bridges"].append({"n": name, "p": [ints(transform(to_m, g).coords) for g in pieces[:4]]})

    s = json.dumps(out, separators=(",", ":"), ensure_ascii=False)
    open(a.out, "w", encoding="utf-8").write(s)
    print("river points", sum(len(r) for p in out["river"] for r in p),
          "| lakes", len(out["lakes"]),
          "| roads", {k: len(v) for k, v in out["roads"].items()},
          "| districts", len(out["districts"]),
          "| bridges", [b["n"] for b in out["bridges"]],
          "| bytes", len(s.encode()))


if __name__ == "__main__":
    main()
