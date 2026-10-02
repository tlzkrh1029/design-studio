() => {
  const inp = document.querySelector('#s-q');
  const cs = getComputedStyle(inp);
  const o = {cw: inp.clientWidth, ow: inp.offsetWidth, pl: cs.paddingLeft, pr: cs.paddingRight, ls: cs.letterSpacing, font: cs.font, type: inp.type};
  inp.value = inp.placeholder; o.sw_value = inp.scrollWidth; inp.value = '';
  const s = document.createElement('span'); s.style.cssText = 'position:absolute;white-space:pre;font:' + cs.font; s.textContent = inp.placeholder; document.body.appendChild(s);
  o.textW = s.getBoundingClientRect().width; s.remove();
  const t = document.createElement('input'); t.type = 'text'; t.style.cssText = 'position:absolute;top:0;left:0;width:257px;height:36px;border:0;padding:0 4px 0 40px;font:' + cs.font; document.body.appendChild(t);
  t.value = inp.placeholder; o.text_sw = t.scrollWidth; o.text_cw = t.clientWidth; t.remove();
  return o;
}
