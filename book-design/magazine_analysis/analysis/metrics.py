import json, io, numpy as np, cv2, pandas as pd
from PIL import Image
from skimage.color import rgb2lab
from sklearn.cluster import KMeans

BASE = '/home/claude/covers/주간지_표지_2026/'
items = json.load(open(BASE + '표지_목록.json', encoding='utf-8'))
ORANGE = np.array([244, 123, 32])

def load_cover(x):
    im = Image.open(BASE + x['filename']).convert('RGB')
    if x['preview_crop_bbox']:
        im = im.crop(tuple(x['preview_crop_bbox']))
    elif x['magazine'] == '한경비즈니스' and im.size == (2230, 2816):
        im = im.crop((120, 120, 2110, 2696))
    return im

def mk_frame(a):
    h, w, _ = a.shape
    def run(line):
        n = 0
        for px in line:
            if np.abs(px.astype(int) - ORANGE).max() < 45: n += 1
            else: break
        return n
    t = run(a[:, w // 2]); b = run(a[::-1, w // 2]); l = run(a[h // 2]); r = run(a[h // 2, ::-1])
    return t, b, l, r

def spectral_residual_saliency(gray):
    g = cv2.resize(gray, (64, int(64 * gray.shape[0] / gray.shape[1])))
    f = np.fft.fft2(g.astype(float))
    la = np.log(np.abs(f) + 1e-9); ph = np.angle(f)
    sr = la - cv2.blur(la, (3, 3))
    sal = np.abs(np.fft.ifft2(np.exp(sr + 1j * ph))) ** 2
    sal = cv2.GaussianBlur(sal, (9, 9), 2.5)
    sal = cv2.resize(sal, (gray.shape[1], gray.shape[0]))
    return sal / sal.max()

rows, palettes = [], {}
for x in sorted(items, key=lambda x: (x['magazine'], x['issue'])):
    im = load_cover(x)
    a_full = np.asarray(im)
    frame = None
    if x['magazine'] == '매경이코노미':
        t, b, l, r = mk_frame(a_full); frame = (t, b, l, r)
        inner = im.crop((l, t, im.width - r, im.height - b))
    else:
        inner = im
    W = 600
    inner = inner.resize((W, round(inner.height * W / inner.width)), Image.LANCZOS)
    a = np.asarray(inner).astype(np.float64)
    lab = rgb2lab(a / 255.0)
    L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]
    C = np.hypot(A, B); H = (np.degrees(np.arctan2(B, A)) + 360) % 360
    R, G, Bc = a[..., 0], a[..., 1], a[..., 2]
    rg = R - G; yb = 0.5 * (R + G) - Bc
    colorfulness = np.sqrt(rg.std() ** 2 + yb.std() ** 2) + 0.3 * np.sqrt(rg.mean() ** 2 + yb.mean() ** 2)
    gray = cv2.cvtColor(a.astype(np.uint8), cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edge_density = (edges > 0).mean()
    hh = gray.shape[0]
    thirds = [(edges[i * hh // 3:(i + 1) * hh // 3] > 0).mean() for i in range(3)]
    buf = io.BytesIO(); inner.save(buf, 'JPEG', quality=75)
    bpp = buf.tell() * 8 / (inner.width * inner.height)
    # smooth (flat) area share as a negative-space proxy
    g32 = gray.astype(np.float32)
    mu = cv2.blur(g32, (9, 9)); var = cv2.blur(g32 * g32, (9, 9)) - mu * mu
    flat_share = (np.sqrt(np.clip(var, 0, None)) < 3.0).mean()
    chroma_mask = C > 15
    warm = ((H < 100) | (H >= 330)) & chroma_mask
    cool = ((H >= 150) & (H < 300)) & chroma_mask
    warm_share = warm.sum() / max(1, chroma_mask.sum())
    achrom_share = (C < 10).mean()
    sal = spectral_residual_saliency(gray)
    ys, xs = np.mgrid[0:sal.shape[0], 0:sal.shape[1]]
    cx = (sal * xs).sum() / sal.sum() / sal.shape[1]; cy = (sal * ys).sum() / sal.sum() / sal.shape[0]
    sym = 1 - np.abs(g32 - g32[:, ::-1]).mean() / 255
    # palette (k-means in Lab on a subsample)
    px = lab.reshape(-1, 3)[::7]
    km = KMeans(n_clusters=5, n_init=4, random_state=0).fit(px)
    counts = np.bincount(km.labels_, minlength=5) / len(km.labels_)
    order = np.argsort(-counts)
    from skimage.color import lab2rgb
    cols = []
    for k in order:
        rgb = (np.clip(lab2rgb(km.cluster_centers_[k][None, None, :])[0, 0], 0, 1) * 255).round().astype(int)
        cols.append(['#%02x%02x%02x' % tuple(rgb), round(float(counts[k]), 3)])
    key = f"{'mk' if x['magazine'] == '매경이코노미' else 'hk'}_{x['issue']}"
    palettes[key] = cols
    rows.append(dict(key=key, magazine=x['magazine'], issue=x['issue'], date=x['publication_date'],
                     L_mean=L.mean(), L_std=L.std(), C_mean=C.mean(), colorfulness=colorfulness,
                     rms_contrast=gray.std() / 255, edge_density=edge_density,
                     edge_top=thirds[0], edge_mid=thirds[1], edge_bot=thirds[2], jpeg_bpp=bpp,
                     flat_share=flat_share, warm_share=warm_share, achrom_share=achrom_share,
                     sal_cx=cx, sal_cy=cy, symmetry=sym, dom_color=cols[0][0], dom_share=cols[0][1],
                     frame=str(frame) if frame else ''))
df = pd.DataFrame(rows)
df.to_csv('/home/claude/covers/analysis/metrics.csv', index=False, encoding='utf-8-sig')
json.dump(palettes, open('/home/claude/covers/analysis/palettes.json', 'w'), ensure_ascii=False)
pd.set_option('display.width', 250)
num = ['L_mean', 'C_mean', 'colorfulness', 'rms_contrast', 'edge_density', 'jpeg_bpp', 'flat_share', 'warm_share', 'achrom_share', 'sal_cx', 'sal_cy', 'symmetry', 'edge_top', 'edge_mid', 'edge_bot']
print(df.groupby('magazine')[num].agg(['mean', 'std']).T.round(3))
print(df[df.magazine == '매경이코노미'].frame.value_counts().head(8))
