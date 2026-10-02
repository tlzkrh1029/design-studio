import sys, json
sys.path.insert(0,'.')
from prep import load
from PIL import Image, ImageDraw, ImageFont
# usage: sheet.py out.jpg y0 y1 cols width key...
out=sys.argv[1]; y0=float(sys.argv[2]); y1=float(sys.argv[3]); cols=int(sys.argv[4]); cw=int(sys.argv[5]); keys=sys.argv[6:]
tiles=[]
for k in keys:
    im=load(k); W,H=im.size
    c=im.crop((0,int(y0*H),W,int(y1*H)))
    h=int(c.size[1]*cw/c.size[0]); c=c.resize((cw,h),Image.LANCZOS)
    d=ImageDraw.Draw(c); d.rectangle((0,0,110,26),fill=(255,0,0)); d.text((4,4),k,fill=(255,255,255))
    tiles.append(c)
th=max(t.size[1] for t in tiles); rows=(len(tiles)+cols-1)//cols
sheet=Image.new('RGB',(cols*cw+(cols-1)*6, rows*th+(rows-1)*6),(40,40,40))
for i,t in enumerate(tiles):
    sheet.paste(t,((i%cols)*(cw+6),(i//cols)*(th+6)))
sheet.save('v/'+out,quality=88); print(sheet.size)
