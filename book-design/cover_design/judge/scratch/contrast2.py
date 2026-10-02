from PIL import Image
from collections import Counter
src='/home/claude/cover_design/judge/calendar_A/'
def lum(c):
    def ch(v):
        v=v/255
        return v/12.92 if v<=0.03928 else ((v+0.055)/1.055)**2.4
    r,g,b=c[:3]
    return 0.2126*ch(r)+0.7152*ch(g)+0.0722*ch(b)
def cr(a,b):
    la,lb=lum(a),lum(b)
    hi,lo=max(la,lb),min(la,lb)
    return (hi+0.05)/(lo+0.05)
def analyze(name,file,box):
    im=Image.open(src+file).convert('RGB')
    px=list(im.crop(box).get_flattened_data()) if hasattr(im,'get_flattened_data') else list(im.crop(box).getdata())
    bg=Counter(px).most_common(1)[0][0]
    dark=min(px,key=lambda c:lum(c))
    print(f'{name:34s} bg={bg} text={dark} contrast~{cr(bg,dark):.2f}')
analyze('P1 다음 호는 10월 1일','P1_s1.png',(1255,1162,1370,1182))
analyze('P1 legend A BTC!','P1_s1.png',(322,144,365,162))
analyze('P1 chart subtitle','P1_s2.png',(72,174,245,192))
analyze('P2 intro text','P2_s1.png',(235,148,595,186))
analyze('P2 chart axis 59.0','P2_s2.png',(1333,806,1362,822))
analyze('P3 chart axis 9/1','P3_s1.png',(1144,1015,1170,1032))
analyze('P3 phase strip num 18','P3_s1.png',(620,236,640,250))
analyze('P4 flow num 12','P4_s2.png',(688,180,708,194))
analyze('P4 legend BTC!','P4_s1.png',(584,172,616,190))
analyze('P5 strip legend','P5_s1.png',(318,125,350,141))
analyze('P5 chart axis','P5_s2.png',(78,252,108,266))
analyze('P6 legend','P6_s1.png',(90,176,135,192))
analyze('P6 table run','P6_s2.png',(1193,636,1280,654))
analyze('P6 chart axis','P6_s2.png',(66,331,98,345))
