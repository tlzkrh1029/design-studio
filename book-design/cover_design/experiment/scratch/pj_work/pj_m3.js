() => {
  const bad = [];
  document.querySelectorAll('body *').forEach(e => {
    if (e.closest('.mz') || e.closest('svg') || e.classList.contains('sr') || e.classList.contains('skip')) return;
    const cs = getComputedStyle(e); if (cs.display === 'none' || cs.position === 'fixed') return;
    const r = e.getBoundingClientRect(); if (!r.width) return;
    const inHeaderBand = e.closest('.masthead') && (e.tagName === 'HEADER');
    if (!['DIV','MAIN','SECTION','FOOTER','HEADER'].includes(e.tagName) || !(r.left === 0 && r.right === 1440)) {
      if (r.left < 71.5 || r.right > 1368.5) bad.push(['OUT', e.tagName, e.className, Math.round(r.left), Math.round(r.right)]);
    }
    if (cs.overflow === 'visible' && e.scrollWidth > e.clientWidth + 1 && e.clientWidth > 0 && cs.display !== 'inline') bad.push(['SW', e.tagName, e.className, e.textContent.slice(0, 20), e.scrollWidth, e.clientWidth]);
  });
  // text boxes that intersect each other inside the 3면 plots and the front page
  const labels = Array.from(document.querySelectorAll('.pl-ref,.pl-zone,.tick,.hol-l'));
  const inter = [];
  for (let i = 0; i < labels.length; i++) for (let j = i + 1; j < labels.length; j++) {
    const a = labels[i].getBoundingClientRect(), b = labels[j].getBoundingClientRect();
    if (a.left < b.right && b.left < a.right && a.top < b.bottom && b.top < a.bottom) inter.push([labels[i].textContent, labels[j].textContent]);
  }
  return {bad: bad.slice(0, 20), inter, docW: document.documentElement.scrollWidth, docH: document.documentElement.scrollHeight, title: document.title,
    fonts: Array.from(document.fonts).filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight + (f.style === 'italic' ? 'i' : '')).filter((v, i, a) => a.indexOf(v) === i).sort()};
}
