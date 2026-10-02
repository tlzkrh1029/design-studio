from PIL import Image
import numpy as np
from scipy import ndimage
from skimage.morphology import skeletonize
def sw(path, box, cond, gh):
    im=np.array(Image.open(path).convert('RGB')).astype(int)
    x0,y0,x1,y1=box
    a=im[y0:y1,x0:x1]; R,G,B=a[...,0],a[...,1],a[...,2]
    m=eval(cond)
    m=ndimage.binary_opening(m,iterations=1)
    m=ndimage.binary_fill_holes(m)&m | m
    dt=ndimage.distance_transform_edt(m)
    sk=skeletonize(m)
    vals=dt[sk]
    w=2*np.median(vals)
    return round(w,1), round(w/gh,3)
jobs=[
 ('hk_1572.jpg',(280,677,610,891),"(R>220)&(G>210)&(B<80)",63),
 ('hk_1573.jpg',(95,605,600,780),"(R>200)&(G>190)&(B<90)",74),
 ('hk_1576.jpg',(180,368,725,442),"(R>200)&(G>180)&(B<90)",70),
 ('hk_1576.jpg',(180,454,725,528),"(R>225)&(G>225)&(B>225)",71),
 ('hk_1589.jpg',(135,850,760,940),"(R>150)&(G>120)&(B<140)&(R-B>40)",82),
 ('hk_1591.jpg',(125,490,780,585),"(R>220)&(G>200)&(B<90)",89),
 ('mk_2342.jpg',(265,365,630,430),"(R>225)&(G>225)&(B>225)",58),
 ('mk_2355.jpg',(180,374,720,436),"(R>225)&(G>225)&(B>225)",55),
 ('mk_2359.jpg',(185,378,715,440),"(R<70)&(G<70)&(B<70)",54),
 ('mk_2360.jpg',(270,350,620,495),"(R<70)&(G<70)&(B<70)",58),
]
for p,b,c,g in jobs:
    print(p,b,sw(p,b,c,g))
