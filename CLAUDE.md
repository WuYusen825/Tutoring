# Working notes for this repo

Lessons from earlier hiccups, so the next session goes smoothly.

- **PDFs**: reportlab/fitz are not installed. Print HTML to PDF with Playwright's Chromium via `_build/pdf.js` (see `beijing-gaokao-english/*/_build/`). `node -e "require('playwright')"` works; do not run `playwright install`.
- **Fit to the page**: a 400-word cloze with tall handwriting lines overflows A4 at 12.5pt / line-height 2.3. 12pt / 1.95 with gaps of `12 + 8*words` mm (max 76) fits one page. Check `pdfinfo` page counts after each build.
- **Word counts**: count with the blanks filled in (`re.sub(r"\{\d+:(.+?)\}", r"\1", text).split()`); the first drafts came out around 360 words, so pad and recount until exactly 400.
- **Pull requests**: this repo has no `main`; the default branch is `claude/vibrant-edison-904o48`. Use `git remote show origin` to find the base before opening a PR.
- **Wording in requests**: the user may write "五个" and "3个" in one sentence; resolve it from the rest of the request (here: 3 passages) and say which was chosen.
- **Editing a user's .docx**: `python-docx` and `pandoc` are not installed. Unzip, edit `word/document.xml` directly (keep each paragraph's run formatting; clone a paragraph and give it a new `w14:paraId` to add one), then repack with `[Content_Types].xml` first: `zip -X out.docx '[Content_Types].xml' && zip -Xr out.docx . -x '[Content_Types].xml'`.
- **docx validation/rendering**: the skill's `validate.py` needs `pip install defusedxml lxml`. `soffice` fails with "source file could not be loaded" (even on a trivial docx) until `apt-get install -y --no-install-recommends libreoffice-writer` is run (about a minute). Then render with `soffice -env:UserInstallation=file://$HOME/lo --headless --convert-to pdf`.
- **Essay-answer requests**: when told "no examples, no quoting the article", write with no quotation marks and check 4-gram overlap against the source passages; keep the existing paragraph layout and leave unmentioned questions untouched. Photographed pages can be incomplete (here p.98 was missing), so rely only on text actually visible.
- **Delivering files (user preference)**: hand finished files (docx, PDF, etc.) to the user directly with `SendUserFile`. Do not commit them to GitHub or open a PR for them unless asked; build them in the scratchpad directory. Only this notes file is committed, because it is the one way these lessons persist across sessions.
