import sys, numpy as np
sys.path.insert(0,'.')
from prep import load
from PIL import Image, ImageFilter
from skimage import color
from collections import deque
from scipy import ndimage as ndi

def cover(key):
    im=load(key)
    if key.startswith('mk'):
        W,H=im.size; f=int(0.04*W)
        im=im.crop((f,f,W-f,H-f))
    return im

def bgmask(key, seeds, tstep=4.0, tseed=25.0, w=240, blur=2):
    im=cover(key); W,H=im.size; h=int(H*w/W)
    s=im.resize((w,h),Image.LANCZOS).filter(ImageFilter.GaussianBlur(blur))
    lab=color.rgb2lab(np.asarray(s)/255.0)
    mask=np.zeros((h,w),bool); q=deque()
    for (fx,fy) in seeds:
        x,y=int(fx*w),int(fy*h); mask[y,x]=True; q.append((y,x,lab[y,x]))
    while q:
        y,x,ref=q.popleft()
        for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
            yy,xx=y+dy,x+dx
            if 0<=yy<h and 0<=xx<w and not mask[yy,xx]:
                d1=np.linalg.norm(lab[yy,xx]-lab[y,x])
                d2=np.linalg.norm(lab[yy,xx]-ref)
                if d1<tstep and d2<tseed:
                    mask[yy,xx]=True; q.append((yy,xx,ref))
    return s, mask

def report(key, seeds, excl, **kw):
    s,mask=bgmask(key,seeds,**kw); h,w=mask.shape
    fg=~mask
    ex=np.zeros_like(fg)
    for (x0,y0,x1,y1) in excl:
        ex[int(y0*h):int(y1*h), int(x0*w):int(x1*w)]=True
    # fill small holes in foreground objects
    fg2=ndi.binary_closing(fg&~ex, iterations=2)
    share=fg2.sum()/fg.size
    # save visualization
    a=np.asarray(s).copy(); a[mask]=(a[mask]*0.3+np.array([0,255,0])*0.7).astype(np.uint8)
    a[ex]=(a[ex]*0.5).astype(np.uint8)
    Image.fromarray(a).resize((w*2,h*2)).save(f'v/area_{key}.png')
    print(key, 'image share (excl. text zones) = %.0f%%'%(share*100))
