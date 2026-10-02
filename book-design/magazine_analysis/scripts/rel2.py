exec(open('load.py').read())
from sklearn.metrics import cohen_kappa_score
c2=[json.loads(l) for f in ['coder2_A.jsonl','coder2_B.jsonl'] for l in open(A+f) if l.strip()]
c2=pd.DataFrame(c2).set_index('key')
c1=df.set_index('key').loc[c2.index]
# 1 format merged
mp=lambda x: '이슈/전망' if x in ('이슈 분석','전망·트렌드') else x
a=c1.format.map(mp); b=c2.format.map(mp)
print('format merged agree',(a==b).mean(),'kappa',cohen_kappa_score(a,b))
print(pd.DataFrame({'c1':c1.format,'c2':c2.format})[c1.format!=c2.format])
# 2 serious_playful
d=(c2.serious_playful.astype(int)-c1.serious_playful.astype(int))
print('serious_playful diff counts', d.value_counts().to_dict())
for v in ['calm_dynamic','minimal_maximal','negative_positive']:
    print(v,(c2[v].astype(int)-c1[v].astype(int)).value_counts().to_dict())
# 3 salience
x=pd.DataFrame({'c1':c1.salience,'c2':c2.salience,'mag':c1.mag})
print(x[x.c1!=x.c2])
print(pd.crosstab([x.mag],[x.c2]),'\n',pd.crosstab([x.mag],[x.c1]))
# 4 weight
x=pd.DataFrame({'c1':c1.weight,'c2':c2.weight,'mag':c1.mag})
print(x[x.c1!=x.c2]); print(pd.crosstab(x.mag,x.c2)); print(pd.crosstab(x.mag,x.c1))
# 5 headline_size
x=pd.DataFrame({'c1':c1.headline_size,'c2':c2.headline_size,'mag':c1.mag})
print(x[x.c1!=x.c2]); print(pd.crosstab(x.mag,x.c2)); print(pd.crosstab(x.mag,x.c1))
# 7 anchorage
x=pd.DataFrame({'c1':c1.anchorage,'c2':c2.anchorage,'mag':c1.mag})
print(x[x.c1!=x.c2])
m2=lambda v:'정박/중복' if v in('정박','중복') else v
print('anch merged agree',(x.c1.map(m2)==x.c2.map(m2)).mean(), cohen_kappa_score(x.c1.map(m2),x.c2.map(m2)))
x=pd.DataFrame({'c1':c1.dependency,'c2':c2.dependency,'mag':c1.mag}); print(x[x.c1!=x.c2])
# image_area disagreements
x=pd.DataFrame({'c1':c1.image_area,'c2':c2.image_area,'mag':c1.mag}); print(x[x.c1!=x.c2])
x=pd.DataFrame({'c1':c1.archetype,'c2':c2.archetype,'mag':c1.mag}); print(x[x.c1!=x.c2])
x=pd.DataFrame({'c1':c1.whitespace,'c2':c2.whitespace,'mag':c1.mag}); print(x[x.c1!=x.c2])
