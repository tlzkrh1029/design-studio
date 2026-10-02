import sys
sys.path.insert(0,'.')
from prep import load
from PIL import Image
# usage: crop.py key x0 y0 x1 y1 (fractions of cover) outname [width]
key=sys.argv[1]; x0,y0,x1,y1=map(float,sys.argv[2:6]); out=sys.argv[6]
w=int(sys.argv[7]) if len(sys.argv)>7 else 1000
im=load(key)
W,H=im.size
c=im.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H)))
h=int(c.size[1]*w/c.size[0])
c.resize((w,h),Image.LANCZOS).save('v/'+out,quality=90)
print(c.size)
