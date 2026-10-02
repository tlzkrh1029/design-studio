() => {
  const out = {};
  function tw(text, font, ls) {
    const s = document.createElement('span');
    s.style.cssText = 'position:absolute;white-space:nowrap;visibility:hidden;font:' + font + ';letter-spacing:' + (ls || '0');
    s.textContent = text; document.body.appendChild(s);
    const w = s.getBoundingClientRect().width; s.remove(); return Math.round(w * 10) / 10;
  }
  out.placeholder = tw('낱말이나 날짜 (예: 안전판, 09.24)', "500 14px/20px 'Gothic A1'");
  const inp = document.querySelector('#s-q');
  out.inputBox = inp.getBoundingClientRect().width;
  out.searchBox = document.querySelector('.search').getBoundingClientRect().width;
  // table header widths
  out.th = Array.from(document.querySelectorAll('.il th')).map(th => {
    const r = th.getBoundingClientRect();
    return { t: th.textContent, w: Math.round(r.width * 10) / 10, h: Math.round(r.height * 10) / 10, sw: th.scrollWidth, cw: th.clientWidth };
  });
  out.thText = tw('ΣSTABLECOIN.D', "700 12px/16px 'Gothic A1'", '.02em');
  // figure values
  out.figs = Array.from(document.querySelectorAll('.fig')).map(f => {
    const v = f.querySelector('.fig-v'); const r = f.getBoundingClientRect();
    return { cell: Math.round(r.width * 10) / 10, valSW: v.scrollWidth, valCW: v.clientWidth, label: f.querySelector('.fig-l').scrollWidth, labelCW: f.querySelector('.fig-l').clientWidth };
  });
  // key boxes
  const box = s => { const e = document.querySelector(s); if (!e) return null; const r = e.getBoundingClientRect(); return [Math.round(r.left*10)/10, Math.round((r.top+scrollY)*10)/10, Math.round(r.width*10)/10, Math.round(r.height*10)/10]; };
  ['.masthead', '.folio', '.plate', '.dbl', '.navbar', '#p1', '.fp', '.fp-cover .cv', '.fp-story', '.fp-top', '#lead-hl', '#verdict', '#read-btn', '#figs', '.fp-side', '.next', '#p2', '.ix-grid', '#p3', '.pm', '.pm-dates', '.pm-lanes', '.pm-legend', '#p4', '.il', '#il-more', '#p5', '.colo-grid', '.imprint'].forEach(s => out[s] = box(s));
  out.docH = document.documentElement.scrollHeight;
  out.docW = document.documentElement.scrollWidth;
  out.leadLines = Math.round(document.querySelector('#lead-hl').scrollHeight / 60);
  out.sideHl = Array.from(document.querySelectorAll('.side-item .item-hl')).map(e => [e.scrollHeight, e.clientHeight]);
  out.ilHl = Array.from(document.querySelectorAll('.il-row:not([hidden]) .il-hl')).map(e => [e.scrollHeight, e.clientHeight]);
  out.rows = Array.from(document.querySelectorAll('.il-row:not([hidden])')).map(e => Math.round(e.getBoundingClientRect().height));
  // overflow check: elements wider than their parents or beyond the container
  const bad = [];
  document.querySelectorAll('body *').forEach(e => {
    if (e.closest('.mz')) return;
    const r = e.getBoundingClientRect();
    if (r.width && (r.right > 1368.5 || r.left < 71.5) && !e.closest('.masthead') && !e.classList.contains('skip') && !e.classList.contains('sr') && getComputedStyle(e).position !== 'fixed') bad.push([e.tagName, e.className, Math.round(r.left), Math.round(r.right)]);
    if (e.scrollWidth > e.clientWidth + 1 && getComputedStyle(e).overflow === 'visible' && e.clientWidth > 0 && !['svg','SVG'].includes(e.tagName)) bad.push(['SW', e.tagName, e.className, e.scrollWidth, e.clientWidth]);
  });
  out.bad = bad.slice(0, 30);
  return out;
}
