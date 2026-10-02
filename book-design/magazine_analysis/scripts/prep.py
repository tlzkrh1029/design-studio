from PIL import Image, ImageChops
import numpy as np, sys, os
MK='/home/claude/covers/주간지_표지_2026/매경이코노미/매경이코노미_2026_제{}호.jpg'
HK='/home/claude/covers/주간지_표지_2026/한경비즈니스/한경비즈니스_2026_제{}호.jpg'
def load(key):
    mag,n=key.split('_')
    if mag=='mk':
        return Image.open(MK.format(n)).convert('RGB')
    if n=='1576':
        im=Image.open(HK.format('1576-1577')).convert('RGB')
    else:
        im=Image.open(HK.format(n)).convert('RGB')
    a=np.asarray(im).astype(int)
    nonwhite=(a.min(axis=2)<235)
    cols=np.where(nonwhite.mean(axis=0)>0.3)[0]
    c0,c1=cols.min(),cols.max()+1
    rows=np.where(nonwhite[:,c0:c1].mean(axis=1)>0.3)[0]
    box=(c0,rows.min(),c1,rows.max()+1)
    return im.crop(box)
def full(key,w=900):
    im=load(key)
    h=int(im.size[1]*w/im.size[0])
    out=f'v/{key}.jpg'
    im.resize((w,h),Image.LANCZOS).save(out,quality=88)
    return im.size
if __name__=='__main__':
    for k in sys.argv[1:]:
        print(k, full(k))
