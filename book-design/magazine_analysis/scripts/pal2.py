exec(open('pal.py').read().split("print('---- MK hue-based')")[0])
for hlo,hhi,cmin in [(40,80,40),(40,80,45),(40,75,40),(38,80,40),(40,70,40),(40,85,40)]:
    sel=P[(P.mag=='mk')&(P.H.between(hlo,hhi))&(P.C>cmin)]
    print('MK',hlo,hhi,cmin, sel.key.nunique(), sorted(set(P[P.mag=='mk'].key)-set(sel.key)))
yel=set(df[(df.mag=='hk')&(df.headline_color=='노랑·금색')].key)
for hlo,hhi,cmin,lmin in [(75,110,50,70),(80,110,50,70),(75,110,40,65),(70,110,40,60),(80,110,60,75),(85,110,70,80)]:
    sel=P[(P.mag=='hk')&(P.H.between(hlo,hhi))&(P.C>cmin)&(P.L>lmin)]
    ks=set(sel.key)
    print('HK',hlo,hhi,cmin,lmin,len(ks),'∩yellowHL',len(ks&yel),'non-yellowHL:',sorted(ks-yel),'yellowHL missing:',sorted(yel-ks))
