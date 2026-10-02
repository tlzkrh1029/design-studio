import json, sys
cb = json.load(open('/home/claude/covers/analysis/codebook.json'))
allowed = {v['var']: v['values'] for c in cb['categories'] for v in c['vars']}
order = [v['var'] for c in cb['categories'] for v in c['vars']]
path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/covers/analysis/coding.jsonl'
existing = {}
try:
    for line in open(path, encoding='utf-8'):
        r = json.loads(line); existing[r['key']] = r
except FileNotFoundError:
    pass
errs = 0
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    r = json.loads(line)
    for var in order:
        if var not in r:
            print('MISSING', r['key'], var); errs += 1; continue
        a = allowed[var]
        if isinstance(a, list) and str(r[var]) not in a:
            print('BAD', r['key'], var, r[var]); errs += 1
        if var in ('calm_dynamic', 'serious_playful', 'minimal_maximal', 'negative_positive') and int(r[var]) not in (1, 2, 3, 4, 5):
            print('BAD', r['key'], var, r[var]); errs += 1
    existing[r['key']] = r
with open(path, 'w', encoding='utf-8') as f:
    for k in sorted(existing, key=lambda k: (k[:2], int(k[3:]))):
        f.write(json.dumps(existing[k], ensure_ascii=False) + '\n')
print('errors', errs, 'total coded', len(existing))
