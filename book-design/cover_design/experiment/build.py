"""Build experiment pages: experiment/<name>.src.html -> experiment/<name>.html
The source may contain <<MZ>> (cover module) and <<COMMON>> (shared helpers), both inside one <script>."""
import sys
root='/home/claude/cover_design/'
mz=open(root+'mz.js',encoding='utf-8').read()
common=open(root+'themes/common.js',encoding='utf-8').read()
for name in sys.argv[1:]:
    s=open(root+'experiment/%s.src.html'%name,encoding='utf-8').read()
    s=s.replace('<<MZ>>',mz).replace('<<COMMON>>',common)
    open(root+'experiment/%s.html'%name,'w',encoding='utf-8').write(s)
    print('built',name,len(s))
