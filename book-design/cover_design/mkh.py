s=open('/home/claude/cover_design/harness.html',encoding='utf-8').read()
m=open('/home/claude/cover_design/mz.js',encoding='utf-8').read()
open('/home/claude/cover_design/h.html','w',encoding='utf-8').write(s.replace('<<MZ>>',m))
