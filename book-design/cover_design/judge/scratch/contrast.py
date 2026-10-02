from PIL import Image
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
    reg=im.crop(box)
    px=list(reg.getdata())
    # background = most common color, text = darkest pixel
    from collections import Counter
    bg=Counter(px).most_common(1)[0][0]
    dark=min(px,key=lambda c:lum(c))
    print(f'{name:28s} bg={bg} text={dark} contrast~{cr(bg,dark):.2f}')
analyze('P1 브리핑없음','P1_s1.png',(735,775,810,797))
analyze('P1 10.2','P1_s1.png',(720,1122,752,1142))
analyze('P1 기록 전','P1_s1.png',(365,328,412,346))
analyze('P2 브리핑없음','P2_s1.png',(755,868,825,890))
analyze('P2 기록 전','P2_s1.png',(360,362,405,378))
analyze('P3 브리핑없음','P3_s1.png',(800,893,875,913))
analyze('P3 기록 전','P3_s1.png',(378,424,422,440))
analyze('P4 브리핑없음','P4_s1.png',(750,779,825,799))
analyze('P4 10.2','P4_s1.png',(730,1106,762,1124))
analyze('P5 브리핑없음','P5_s1.png',(730,774,800,794))
analyze('P5 10.2','P5_s1.png',(710,1110,742,1128))
analyze('P6 브리핑없음','P6_s1.png',(728,788,800,808))
analyze('P6 10.2','P6_s1.png',(708,1141,740,1160))
