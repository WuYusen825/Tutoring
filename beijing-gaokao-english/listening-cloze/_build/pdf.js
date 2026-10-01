// Print HTML files to A4 PDFs with Playwright's Chromium.
// Usage: node pdf.js in.html out.pdf [in2.html out2.pdf ...]
const path = require('path');
const { chromium } = require('playwright');

const FOOTER = `<div style="width:100%;text-align:center;font-size:8pt;color:#666;
  font-family:'Songti SC','SimSun','Noto Sans CJK SC','WenQuanYi Zen Hei',sans-serif;">
  第 <span class="pageNumber"></span> 页（共 <span class="totalPages"></span> 页）</div>`;

(async () => {
  const args = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (let i = 0; i < args.length; i += 2) {
    const src = path.resolve(args[i]);
    const out = path.resolve(args[i + 1]);
    await page.goto('file://' + src, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({
      path: out,
      format: 'A4',
      printBackground: true,
      margin: { top: '16mm', bottom: '18mm', left: '18mm', right: '18mm' },
      displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: FOOTER,
    });
    console.log('  ' + path.basename(out));
  }
  await browser.close();
})().catch(err => {
  console.error(err);
  process.exit(1);
});
