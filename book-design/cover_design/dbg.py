import asyncio, json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':2200,'height':1200})
        await pg.goto('file:///home/claude/cover_design/h.html#catalog&n=8&cw=220')
        await pg.wait_for_selector('body[data-ready]'); await pg.wait_for_timeout(300)
        r=await pg.evaluate('''()=>{var out=[]; document.querySelectorAll('.mz').forEach(function(c,i){var mn=c.querySelector('.m-main'), hb=c.querySelector('.m-hb');
          var cs=getComputedStyle(mn); var W=c.offsetWidth/100; var f=parseFloat(mn.style.fontSize);
          if(mn.scrollHeight>mn.clientHeight+1) out.push({i:i, scene:c.getAttribute('data-scene'), fs:mn.style.fontSize, clamp:mn.style.webkitLineClamp, sh:mn.scrollHeight, ch:mn.clientHeight, lh:cs.lineHeight, hbH:hb.clientHeight, hbSH:hb.scrollHeight, text:mn.textContent});});
          return out;}''')
        print(json.dumps(r,ensure_ascii=False,indent=1))
        await b.close()
asyncio.run(main())
