import sys
from PIL import Image
import numpy as np
from skimage import color
def stats(k):
    im=np.array(Image.open(f'/home/claude/covers/analysis/single/{k}.jpg').convert('RGB'))/255.0
    lab=color.rgb2lab(im)
    L=lab[...,0]; a=lab[...,1]; b=lab[...,2]
    C=np.hypot(a,b); h=(np.degrees(np.arctan2(b,a))+360)%360
    H=im.shape[0]
    print(k, 'mean L*=%.1f'%L.mean(), 'mean C*=%.1f'%C.mean())
    for i,(y0,y1) in enumerate([(0,H//3),(H//3,2*H//3),(2*H//3,H)]):
        print('  third',i,'L=%.1f C=%.1f'%(L[y0:y1].mean(),C[y0:y1].mean()))
    chrom=C>15
    print('  achromatic share %.2f'%(1-chrom.mean()))
    bins=[(335,50,'red-pink'),(50,105,'orange-yellow'),(105,230,'green-cyan'),(230,310,'blue'),(310,335,'purple')]
    hh=h[chrom]
    tot=chrom.sum()
    for lo,hi,n in bins:
        if n.startswith('red'):
            m=((hh>=335)|(hh<50))
        else:
            m=(hh>=lo)&(hh<hi)
        print('   %s %.2f'%(n,m.sum()/L.size))
for k in sys.argv[1:]:
    stats(k)
