exec(open('load.py').read())
from sklearn.metrics import cohen_kappa_score
c2=[json.loads(l) for f in ['coder2_A.jsonl','coder2_B.jsonl'] for l in open(A+f) if l.strip()]
c2=pd.DataFrame(c2).set_index('key')
c1=df.set_index('key').loc[c2.index]
cb=json.load(open(A+'codebook.json'))
order={}
for c in cb['categories']:
    for v in c['vars']:
        order[v['var']]=v['values']
ordinal={'weight','headline_size','image_area','whitespace','bg_value','depth','headline_v','secondary_lines','headline_lines','calm_dynamic','serious_playful','minimal_maximal','negative_positive'}
res=[]
for v in order:
    if order[v] in ('자유 기록','없음 또는 대상 기록') or v in('headline','key_symbols','reference'): continue
    a=c1[v].astype(str); b=c2[v].astype(str)
    agree=(a==b).mean()
    k=cohen_kappa_score(a,b)
    kw=None
    if v in ordinal:
        if isinstance(order[v],list):
            m={x:i for i,x in enumerate(order[v])}
            try:
                ai=a.map(m); bi=b.map(m)
                kw=cohen_kappa_score(ai,bi,weights='linear',labels=list(range(len(order[v]))))
            except Exception as e: kw=str(e)
        else:
            kw=cohen_kappa_score(a.astype(int),b.astype(int),weights='linear')
    res.append((v,agree,k,kw))
R=pd.DataFrame(res,columns=['var','agree','k','kw'])
rel=pd.read_csv(A+'reliability.csv',encoding='utf-8-sig')
X=R.merge(rel[['var','agree','kappa','kappa_w','k_final']],on='var',suffixes=('','_rel'))
X['kf']=X.apply(lambda r: r.kw if r.kw is not None and not isinstance(r.kw,str) else r.k,axis=1)
pd.set_option('display.width',250)
print(X.to_string())
print(len(X),'mean agree',X.agree.mean(),'median kf',X.kf.median())
