import sys
from PIL import Image
import numpy as np
def runs1d(v):
    out=[];c=0
    for x in v:
        if x: c+=1
        elif c: out.append(c); c=0
    if c: out.append(c)
    return out
def stroke(path, box, cond):
    im=np.array(Image.open(path).convert('RGB')).astype(int)
    x0,y0,x1,y1=box
    a=im[y0:y1,x0:x1]; R,G,B=a[...,0],a[...,1],a[...,2]
    m=eval(cond)
    hr=[];vr=[]
    for row in m: hr+=runs1d(row)
    for col in m.T: vr+=runs1d(col)
    hr=[r for r in hr if r>2]; vr=[r for r in vr if r>2]
    rows=np.where(m.sum(1)>0)[0]
    gh=rows.max()-rows.min()+1 if len(rows) else 0
    print(path, box, 'glyph h',gh,'median horiz run',np.median(hr),'median vert run',np.median(vr),'ratio',round(min(np.median(hr),np.median(vr))/gh,3))
if __name__=='__main__':
    stroke(sys.argv[1], tuple(map(int,sys.argv[2].split(','))), sys.argv[3])
