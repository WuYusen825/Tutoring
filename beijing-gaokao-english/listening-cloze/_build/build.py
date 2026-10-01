#!/usr/bin/env python3
"""Build the listening-cloze handouts from content.py.

    python3 _build/build.py          # print the A4 PDFs into ../pdf/
                                     # (needs: Node.js with the playwright package and its Chromium)
"""
import html
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PDF_DIR = ROOT / "pdf"
PRINT_DIR = HERE / ".print"
sys.path.insert(0, str(HERE))
from content import PASSAGES  # noqa: E402

BLANK_RE = re.compile(r"\{(\d+):(.+?)\}")

INSTR = ("听力记忆填空：教师（或录音）朗读两遍，学生边听边记，再凭记忆在横线上补全空缺的内容"
         "（每空 3–8 个词），最后对照答案页订正。")


def gap_mm(answer):
    return min(76, 12 + 8 * len(answer.split()))


def paras(text):
    return [p.strip() for p in text.strip().split("\n\n") if p.strip()]


def render(text, mode):
    """mode 'blank': numbered gaps; mode 'answer': red bold answers."""
    def sub(m):
        n, ans = m[1], html.escape(m[2])
        if mode == "blank":
            return (f'<span class="no">({n})</span>'
                    f'<span class="gap" style="width:{gap_mm(m[2]):.0f}mm"></span>')
        return f'<span class="no">({n})</span><b>{ans}</b>'
    parts, last = [], 0
    for m in BLANK_RE.finditer(text):
        parts.append(html.escape(text[last:m.start()]))
        parts.append(sub(m))
        last = m.end()
    parts.append(html.escape(text[last:]))
    return "".join(parts)


def word_count(text):
    return len(BLANK_RE.sub(r"\2", text).split())


def student_page(p):
    body = "".join(f"<p>{render(t, 'blank')}</p>" for t in paras(p["text"]))
    return f"""<section class="page">
<h2>短文 {p['id']}<span>{html.escape(p['title'])}</span></h2>
<p class="tag">{html.escape(p['tag'])}　·　{word_count(p['text'])} 词</p>
<p class="instr">{INSTR}</p>
<div class="cloze en">{body}</div>
</section>"""


def answer_page(p):
    pairs = BLANK_RE.findall(p["text"])
    half = (len(pairs) + 1) // 2
    rows = "".join(
        "<tr>" + "".join(
            f'<td class="n">{n}</td><td class="a en">{html.escape(a)}</td>'
            for n, a in (pairs[i], pairs[i + half]))
        + "</tr>" for i in range(half))
    body = "".join(f"<p>{render(t, 'answer')}</p>" for t in paras(p["text"]))
    vocab = "　".join(f"<b class='en'>{html.escape(en)}</b> {html.escape(cn)}" for en, cn in p["vocab"])
    return f"""<section class="page answers">
<h2>短文 {p['id']} 参考答案<span>{html.escape(p['title'])}</span></h2>
<table class="key">{rows}</table>
<div class="cloze en">{body}</div>
<p class="vocab" style="margin-top:3mm">词汇：{vocab}</p>
</section>"""


def page_html(body):
    css = (HERE / "print.css").read_text(encoding="utf-8")
    return f'<!doctype html><html lang="zh"><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


def main():
    PRINT_DIR.mkdir(exist_ok=True)
    PDF_DIR.mkdir(exist_ok=True)
    students = "".join(student_page(p) for p in PASSAGES)
    answers = "".join(answer_page(p) for p in PASSAGES)
    jobs = {
        "listening-cloze": students + answers,
        "listening-cloze-student": students,
    }
    args = []
    for name, body in jobs.items():
        src = PRINT_DIR / f"{name}.html"
        src.write_text(page_html(body), encoding="utf-8")
        args += [str(src), str(PDF_DIR / f"{name}.pdf")]
    env = dict(os.environ)
    try:  # let node find a globally installed playwright
        root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
        env["NODE_PATH"] = os.pathsep.join(p for p in (env.get("NODE_PATH"), root) if p)
    except FileNotFoundError:
        pass
    subprocess.run(["node", str(HERE / "pdf.js"), *args], check=True, env=env)


if __name__ == "__main__":
    main()
