import json, pandas as pd, numpy as np
A='/home/claude/covers/analysis/'
rows=[json.loads(l) for l in open(A+'coding.jsonl') if l.strip()]
df=pd.DataFrame(rows)
meta=json.load(open('/home/claude/covers/주간지_표지_2026/표지_목록.json'))
md=pd.DataFrame(meta)
md['key']=md.apply(lambda r:('mk_' if r.magazine=='매경이코노미' else 'hk_')+str(r.issue),axis=1)
df=df.merge(md[['key','publication_date','combined_issues','note','width','height']],on='key',how='left')
df['mag']=df.key.str[:2]
df['month']=pd.to_datetime(df.publication_date).dt.month
df['Q']=((df.month-1)//3+1)
met=pd.read_csv(A+'metrics.csv',encoding='utf-8-sig')
N={'mk':38,'hk':37}
def pct(n,d): return round(100*n/d)
def dist(var, mag=None, sub=None):
    d=df if sub is None else sub
    out={}
    for m in (['mk','hk'] if mag is None else [mag]):
        s=d[d.mag==m][var]
        vc=s.value_counts()
        out[m]=[(k,int(v),f'{100*v/len(s):.1f}%') for k,v in vc.items()]
    return out
