# Working notes for this repo

Lessons from earlier hiccups, so the next session goes smoothly.

- **PDFs**: reportlab/fitz are not installed. Print HTML to PDF with Playwright's Chromium via `_build/pdf.js` (see `beijing-gaokao-english/*/_build/`). `node -e "require('playwright')"` works; do not run `playwright install`.
- **Fit to the page**: a 400-word cloze with tall handwriting lines overflows A4 at 12.5pt / line-height 2.3. 12pt / 1.95 with gaps of `12 + 8*words` mm (max 76) fits one page. Check `pdfinfo` page counts after each build.
- **Word counts**: count with the blanks filled in (`re.sub(r"\{\d+:(.+?)\}", r"\1", text).split()`); the first drafts came out around 360 words, so pad and recount until exactly 400.
- **Pull requests**: this repo has no `main`; the default branch is `claude/vibrant-edison-904o48`. Use `git remote show origin` to find the base before opening a PR.
- **Wording in requests**: the user may write "五个" and "3个" in one sentence; resolve it from the rest of the request (here: 3 passages) and say which was chosen.
