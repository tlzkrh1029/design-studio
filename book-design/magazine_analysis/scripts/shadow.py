import sys
from PIL import Image
import numpy as np
from scipy import ndimage
def check(path, box, cond):
    im=np.array(Image.open(path).convert('RGB')).astype(float)
    x0,y0,x1,y1=box
    a=im[y0:y1,x0:x1]; R,G,B=a[...,0],a[...,1],a[...,2]
    m=eval(cond)
    m=ndimage.binary_opening(m,iterations=1)
    lum=a.mean(2)
    res={}
    for name,(dx,dy) in {'down-right':(1,1),'up-left':(-1,-1),'down':(0,1),'up':(0,-1),'right':(1,0),'left':(-1,0)}.items():
        vals=[]
        for d in range(3,8):
            sh=np.roll(np.roll(m,dy*d,0),dx*d,1)
            band=sh&~ndimage.binary_dilation(m,iterations=2)
            vals.append(lum[band].mean())
        res[name]=round(float(np.mean(vals)),1)
    # outline check: ring 1-2 px around glyph
    ring=ndimage.binary_dilation(m,iterations=2)&~m
    ring_far=ndimage.binary_dilation(m,iterations=10)&~ndimage.binary_dilation(m,iterations=6)
    print(path,box,res,'ring(1-2px)',round(float(lum[ring].mean()),1),'far(6-10px)',round(float(lum[ring_far].mean()),1))
if __name__=='__main__':
    check(sys.argv[1], tuple(map(int,sys.argv[2].split(','))), sys.argv[3])
