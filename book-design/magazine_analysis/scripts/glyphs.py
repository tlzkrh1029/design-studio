import sys
from PIL import Image
import numpy as np
from scipy import ndimage
def glyphs(path, box, cond, minw=5):
    im=np.array(Image.open(path).convert('RGB')).astype(int)
    x0,y0,x1,y1=box
    a=im[y0:y1,x0:x1]; R,G,B=a[...,0],a[...,1],a[...,2]
    m=eval(cond)
    m=ndimage.binary_opening(m,iterations=1)
    lab,n=ndimage.label(m)
    objs=ndimage.find_objects(lab)
    hs=[]
    for i,sl in enumerate(objs):
        h=sl[0].stop-sl[0].start; w=sl[1].stop-sl[1].start
        area=(lab[sl]==i+1).sum()
        if area>150:
            hs.append((x0+sl[1].start,y0+sl[0].start,y0+sl[0].stop-1,h,w,area))
    hs.sort()
    for t in hs: print('x%d y%d-%d h%d w%d area%d'%t)
    H=im.shape[0]
    allrows=np.where(m.sum(1)>0)[0]
    print('overall rows',y0+allrows.min(),y0+allrows.max(),'H',H)
if __name__=='__main__':
    glyphs(sys.argv[1], tuple(map(int,sys.argv[2].split(','))), sys.argv[3])
