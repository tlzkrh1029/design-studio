import asyncio, json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':2200,'height':1200})
        await pg.goto('file:///home/claude/cover_design/h.html#catalog&n=8&cw=220')
        await pg.wait_for_selector('body[data-ready]'); await pg.wait_for_timeout(300)
        r=await pg.evaluate('''()=>{var c=document.querySelectorAll('.mz')[4], mn=c.querySelector('.m-main'); var o={};
          mn.style.webkitLineClamp='unset'; o.unset=mn.scrollHeight;
          mn.style.webkitLineClamp='2'; o.c2=mn.scrollHeight;
          mn.style.webkitLineClamp='3'; o.c3=mn.scrollHeight;
          mn.style.webkitLineClamp='unset'; o.unset2=mn.scrollHeight; o.w=mn.clientWidth;
          mn.style.textWrap='wrap'; o.nobal=mn.scrollHeight; mn.style.textWrap='';
          var r=document.createRange(); r.selectNodeContents(mn); o.rects=Array.from(r.getClientRects()).map(function(x){return [Math.round(x.left),Math.round(x.top),Math.round(x.width)];});
          return o;}''')
        print(json.dumps(r,ensure_ascii=False))
        await b.close()
asyncio.run(main())
