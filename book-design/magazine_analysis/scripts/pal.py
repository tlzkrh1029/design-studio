exec(open('load.py').read())
import numpy as np
pal=json.load(open(A+'palettes.json'))
def hex2lab(h):
    rgb=np.array([int(h[i:i+2],16) for i in (1,3,5)])/255.0
    rgb=np.where(rgb<=0.04045,rgb/12.92,((rgb+0.055)/1.055)**2.4)
    M=np.array([[0.4124564,0.3575761,0.1804375],[0.2126729,0.7151522,0.0721750],[0.0193339,0.1191920,0.9503041]])
    xyz=M@rgb/np.array([0.95047,1.0,1.08883])
    f=np.where(xyz>0.008856,np.cbrt(xyz),7.787*xyz+16/116)
    L=116*f[1]-16; a=500*(f[0]-f[1]); b=200*(f[1]-f[2])
    return np.array([L,a,b])
orange=hex2lab('#f47b20')
rows=[]
for k,cols in pal.items():
    for h,s in cols:
        lab=hex2lab(h); C=np.hypot(lab[1],lab[2]); H=np.degrees(np.arctan2(lab[2],lab[1]))%360
        rows.append((k,h,s,lab[0],C,H,np.linalg.norm(lab-orange)))
P=pd.DataFrame(rows,columns=['key','hex','share','L','C','H','dE_or'])
P['mag']=P.key.str[:2]
for th in [10,12,15,18,20,25,30]:
    n=P[(P.mag=='mk')&(P.dE_or<th)].key.nunique()
    print('MK orange dE<',th,':',n)
print('MK hues of nearest-orange per cover:')
mk=P[P.mag=='mk'].sort_values('dE_or').groupby('key').first()
print(mk[['hex','share','L','C','H','dE_or']].sort_values('dE_or').to_string())
print('---- MK hue-based')
for hlo,hhi,cmin in [(45,70,55),(40,70,50),(45,65,55),(40,75,50),(35,75,45),(45,70,60)]:
    sel=P[(P.mag=='mk')&(P.H.between(hlo,hhi))&(P.C>cmin)]
    print(hlo,hhi,cmin, sel.key.nunique())
print('---- HK yellow candidates')
for hlo,hhi,cmin,lmin in [(70,100,40,60),(65,100,40,55),(70,105,35,60),(60,100,45,60),(75,100,50,65),(70,100,50,60),(65,95,45,60)]:
    sel=P[(P.mag=='hk')&(P.H.between(hlo,hhi))&(P.C>cmin)&(P.L>lmin)]
    ks=set(sel.key)
    yel=set(df[(df.mag=='hk')&(df.headline_color=='노랑·금색')].key)
    print(hlo,hhi,cmin,lmin,'n',len(ks),'of which yellow headline',len(ks&yel),'yellow-headline covers total',len(yel))
hk=P[P.mag=='hk'].copy()
hk['yl']=hk.H.between(65,105)&(hk.C>35)&(hk.L>55)
d=df.set_index('key')
for k,g in hk.groupby('key'):
    y=g[g.yl]
    print(k, d.loc[k,'headline_color'], d.loc[k,'bg_hue'], ' '.join(f'{r.hex}({r.share:.3f},L{r.L:.0f},C{r.C:.0f},H{r.H:.0f})' for r in g.itertuples()), '| YELLOW' if len(y) else '')
