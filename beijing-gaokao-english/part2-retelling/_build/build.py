#!/usr/bin/env python3
"""Build the Part 2 practice materials from content.py.

    python3 _build/build.py            # Markdown sheets + practice page
    python3 _build/build.py --audio    # also re-synthesise the MP3s
                                       # (needs: pip install edge-tts imageio-ffmpeg, and network)
    python3 _build/build.py --pdf      # also print the PDFs
                                       # (needs: Node.js with the playwright package and its Chromium)
"""
import argparse
import asyncio
import html
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
AUDIO = ROOT / "audio"
DURATIONS = AUDIO / "durations.json"
PDF_DIR = ROOT / "pdf"
PRINT_DIR = HERE / ".print"
sys.path.insert(0, str(HERE))
from content import PASSAGES, SETS  # noqa: E402

BLANK = "＿＿＿＿＿＿"

SOURCES = [
    ("北京市2025年高考英语听说机考问答（首都之窗）",
     "https://www.beijing.gov.cn/fuwu/bmfw/sy/jrts/202411/t20241118_3942798.html"),
    ("2024年北京高考英语听说考备考技巧——听后转述题（北京高考在线）",
     "https://www.gaokzx.com/c/202403/92048.html"),
    ("2026北京高考英语听说考备考指南：听后转述（北京高考在线）",
     "https://www.gaokzx.com/gk/gaokao/149636.html"),
    ("北京2025年第一次高考英语听说考备考全攻略（搜狐）",
     "https://m.sohu.com/a/832124006_121124317/"),
]


# ---------- text helpers ----------

def paras(text):
    return [p.strip() for p in text.strip().split("\n\n") if p.strip()]


def plain(text):
    return re.sub(r"\{(\w+)\}", r"\1", text.replace(" / ", " "))


def words(text):
    return len(re.sub(r"\[\[|\]\]", "", plain(text)).split())


def fmt_dur(sec):
    if not sec:
        return "—"
    sec = round(sec)
    return f"{sec // 60}:{sec % 60:02d}"


def load_durations():
    try:
        return json.loads(DURATIONS.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}


def detail(text, s, mode):
    """Render a table detail; mode 'blank' leaves gaps, 'answer' fills them in bold."""
    def sub(m):
        n = int(m[1])
        if mode == "blank":
            return f"（{n}）{BLANK}"
        return f"（{n}）**{s['answers'][n - 1]['word']}**"
    return re.sub(r"\[(\d)\]", sub, text)


def cell(items):
    if len(items) == 1:
        return items[0]
    return "<br>".join(f"• {i}" for i in items)


def table_rows(s):
    return [r for r in s["rows"] if r.get("in_table", True)]


def pron(s):
    return {"she": "she / her", "he": "he / his"}[s["pronoun"]]


# ---------- Markdown ----------

# (heading, points, instruction) for the two sections of every set
RECORD = (
    "第一节　听后记录", "（共 4 小题；每小题 1.5 分，共 6 分）",
    "你将听到一段独白。请根据所听内容，完成下面的信息记录表。每空只填一个单词。"
    "独白读两遍。你将有 60 秒的时间阅读表格。",
)
RETELL = (
    "第二节　听后转述", "（共 9 分）",
    "你将再听一遍这段独白。请根据所听内容和信息记录表，用英语转述独白内容。"
    "你将有 2 分钟的准备时间，然后在 2 分钟内完成转述。转述的开头已给出。",
)
INSTR_RECORD = f"**{RECORD[0]}**{RECORD[1]}\n\n{RECORD[2]}"
INSTR_RETELL = f"**{RETELL[0]}**{RETELL[1]}\n\n{RETELL[2]}"
SHEET_TITLE = "学生版 · 第二部分 听后记录和转述（5 套）"
SHEET_NOTES = [
    "每套流程：读表 60 秒 → 听两遍，填 4 个空 → 再听第三遍 → 准备 2 分钟 → 转述 2 分钟。",
    "听的时候在草稿纸上画两栏：左边记要点，右边记表格里**没有**的细节（转述加分靠它）。",
]


def md_student():
    out = [f"# {SHEET_TITLE}", "", *[f"> {n}" for n in SHEET_NOTES], ""]
    for s in SETS:
        out += [
            "---", "",
            f"## 第 {s['id']} 套",
            "",
            INSTR_RECORD,
            "",
            f"| **{s['title']}** | |",
            "|---|---|",
        ]
        for r in table_rows(s):
            out.append(f"| {r['main']} | {cell([detail(t, s, 'blank') for t in r['table']])} |")
        out += [
            "",
            INSTR_RETELL,
            "",
            f"> **{s['opening']}** ……",
            "",
        ]
    return "\n".join(out)


def md_teacher(durs):
    out = [
        "# 教师版 · 原文、答案、评分清单与参考转述",
        "",
        "> 学生做完再看。评分清单里“表格内信息”必须全部说到；“表格外细节”至少补 3 条、且来自不同要点，才有机会拿满分。",
        "",
    ]
    for s in SETS:
        out.append(f"- [第 {s['id']} 套　{s['title']}（{s['topic_cn']}）](#set{s['id']})")
    out.append("")
    for s in SETS:
        audio = f"audio/{s['slug']}.mp3"
        out += [
            "---", "",
            f'<a id="set{s["id"]}"></a>',
            "",
            f"## 第 {s['id']} 套　{s['title']}",
            "",
            f"- 主题：{s['theme']}｜题材：{s['genre']}",
            f"- 说话人：{s['speaker']} → 转述用 **{pron(s)}**",
            f"- 音频：[`{audio}`]({audio})（{fmt_dur(durs.get(s['slug']))}，{words(s['script'])} 词）",
            "",
            "### 听后记录答案",
            "",
            "| 空 | 答案 | 说明 |",
            "|---|---|---|",
        ]
        for i, a in enumerate(s["answers"], 1):
            out.append(f"| {i} | **{a['word']}** | {a['note']} |")
        out += [
            "",
            "### 转述评分清单",
            "",
            f"转述开头（已给出）：*{s['opening']}*",
            "",
            "| 要点 | 表格内信息（必须说到） | 表格外细节（可补充） |",
            "|---|---|---|",
        ]
        for r in s["rows"]:
            inside = cell([detail(t, s, "answer") for t in r["table"]]) if r["table"] else "（表格中没有）"
            main = r["main"] if r.get("in_table", True) else f"{r['main']}（表格外）"
            out.append(f"| {main} | {inside} | {cell(r['extras'])} |")
        model = re.sub(r"\[\[(.+?)\]\]", r"**\1**", s["model"])
        mp = paras(model)
        mp[0] = f"*{s['opening']}* {mp[0]}"
        out += [
            "",
            f"### 参考转述（约 {words(s['opening'] + ' ' + s['model'])} 词，粗体为衔接词和转述动词）",
            "",
            *sum(([f"> {p}", ">"] for p in mp), [])[:-1],
            "",
            "### 易错点",
            "",
            *[f"- {p}" for p in s["pitfalls"]],
            "",
            "### 词汇",
            "",
            "｜".join(f"{en} {cn}" for en, cn in s["vocab"]),
            "",
            "### 听力原文（粗体为填空答案）",
            "",
        ]
        for p in paras(s["script"]):
            out += [re.sub(r"\{(\w+)\}", r"**\1**", p.replace(" / ", " ")), ""]
    return "\n".join(out)


SENSE_INTRO = """# 断句练习 · 意群停顿（配合第三部分朗读）

第三部分短文朗读时，断句（意群停顿）直接影响流利度和语调。断句问题一般有两种：一是停在不该停的地方（冠词和名词中间、介词和宾语中间），二是一口气读到没气，只好在句子中间乱停。下面 5 篇就是第二部分的听力原文，已经标好意群，可以直接配合音频跟读。

## 标记说明

- 标点处自然停顿（逗号短停，句号稍长），不再重复标注。
- **/** 表示这里没有标点，但可以稍作停顿（半拍）。
- 录音里不是每个 **/** 都有明显停顿，语速快时可以连着读过去；但绝不能停在一个意群的中间。

## 可以停的位置

1. 长主语之后：The blue light from screens **/** tells your brain …
2. that / what / whether / who 等引导的从句前：… tells your brain **/** that it's still daytime
3. 较长的介词短语、状语前：… put away your phone **/** at least half an hour before bed
4. and / or 连接较长的并列成分时，停在连词前：… pick out the main points **/** and put them into their own words
5. 句首状语之后（多数有逗号）：In fact, … / After class, … / Last summer, …

## 绝不能停的位置

| 结构 | 错误示范 |
|---|---|
| 冠词 / 物主代词 + 名词 | the / school ✗ |
| 介词 + 宾语 | from / screens ✗ |
| 短语动词 | put / away ✗　pick / out ✗ |
| to + 动词原形 | to / fall asleep ✗ |
| 助动词、情态动词 + 动词 | can / help ✗ |
| 形容词 + 名词 | long-term / memory ✗ |

## 练习步骤（每篇约 10 分钟）

1. 听录音，看划分版，手指跟着意群走。
2. 逐个意群跟读：一个意群一口气读完，意群内部连读，停顿只停半拍。
3. 拿教师版里没有标记的原文，自己用铅笔划意群，再和这里对照。
4. 整段录音，回听时只查一件事：有没有停在“绝不能停”的位置。
"""


def md_sense():
    out = [SENSE_INTRO]
    for s in SETS:
        out += [
            "---", "",
            f"## 第 {s['id']} 套　{s['title']}",
            "",
            f"音频：[`audio/{s['slug']}.mp3`](audio/{s['slug']}.mp3)",
            "",
        ]
        for p in paras(s["script"]):
            out += [re.sub(r"\{(\w+)\}", r"\1", p).replace(" / ", " **/** "), ""]
    return "\n".join(out)


def md_passages():
    out = ["# 短文 1–5", ""]
    for i, p in enumerate(PASSAGES, 1):
        out += [f"## 短文 {i}", ""]
        for x in paras(p):
            out += [x, ""]
    return "\n".join(out)


def md_readme(durs):
    rows = "\n".join(
        f"| {s['id']} | {s['title']}（{s['topic_cn']}） | {s['genre']} | {s['speaker']} | "
        f"{fmt_dur(durs.get(s['slug']))} | {words(s['script'])} |"
        for s in SETS
    )
    sources = "\n".join(f"- [{t}]({u})" for t, u in SOURCES)
    return f"""# 北京高考英语听说 · 第二部分「听后记录和转述」专项训练

5 套原创模拟题，按北京高考英语听说机考第二部分的完整流程设计：同一段独白先做**听后记录**（4 个空），再做**听后转述**（开头已给出）。每套都有音频、学生版记录表、教师版答案 / 评分清单 / 参考转述，另附一份标好意群的原文，可用于第三部分朗读的断句练习。

另有 5 篇记忆短文（3 篇 80 词、2 篇 150 词，由短到长），结构依次对应 5 套听力的题材，用来做转述前的记忆练习。

> 题目是原创的仿真题，不是真题原文。题型、时间和分值依据公开的考试信息和备考资料整理（见文末）。官方真题练习可用北京教育考试院的英语听说考试练习系统（elst.bjeea.cn）。

## 文件

| 文件 | 用途 |
|---|---|
| [pdf/passages-and-student-sheets.pdf](pdf/passages-and-student-sheets.pdf) | 打印用：短文 1–5 在前，学生版在后（A4） |
| [pdf/student-sheets.pdf](pdf/student-sheets.pdf)、[pdf/passages.pdf](pdf/passages.pdf) | 同样的内容，分成两个文件 |
| [passages.md](passages.md) | 记忆短文 1–5 的文本版 |
| [student-sheets.md](student-sheets.md) | 学生版：答题说明、记录表、转述开头，可打印或投屏 |
| [teacher-key.md](teacher-key.md) | 教师版：填空答案、转述评分清单、参考转述、易错点、听力原文 |
| [sense-groups.md](sense-groups.md) | 断句练习：意群停顿规则，5 篇原文的断句划分 |
| [audio/](audio/) | 5 段独白录音，每个文件只录一遍，按下面的流程播放三遍 |
| [practice.html](practice.html) | 模拟练习页：自动播放三遍，读表、准备、转述都有倒计时，可以核对填空、用评分清单打分 |

## 5 套题一览

| 套 | 题目 | 题材 | 说话人 | 时长 | 词数 |
|---|---|---|---|---|---|
{rows}

题材有意做了区分：建议类、事物介绍、问题—措施、研究报告、第一人称经历。它们各自考不同的转述能力，比如祈使句要改成转述结构，第一人称要改成第三人称，研究过程要用过去时。

## 第二部分怎么考

| 环节 | 内容 | 时间 | 分值 |
|---|---|---|---|
| 听后记录 | 独白播放两遍，完成 4 个空（本练习每空一词） | 播放前有 60 秒读表 | 4 × 1.5 = 6 分 |
| 听后转述 | 独白再播放一遍，根据所听内容和记录表转述，开头已给出 | 准备 120 秒，转述 120 秒 | 9 分 |

## 课堂使用流程（每套约 12 分钟）

1. **读表 60 秒**：浏览表格，预测每个空的词性和形式（单复数、时态、比较级等）。
2. **放第一遍，停约 10 秒，再放第二遍**：边听边填空，同时在草稿纸上速记表格外的细节。
3. **放第三遍**：重点补记表格外的细节。
4. **准备 120 秒**：按表格顺序在心里串一遍，想好每个要点下补哪条细节、用什么衔接词。
5. **转述 120 秒**：从给定的开头说起，最好用手机录下来。
6. **讲评**：对照教师版的评分清单打勾，然后再听一遍原文、读一遍参考转述，让学生重说一次。

> 两遍之间的 10 秒间隔和第二遍后的检查时间是练习设定，真实考试以机考提示为准。

## 转述怎么拿高分

- 内容比语言权重大。表格里的信息（包括 4 个空）要全部说到。
- 想拿满分，还要补表格外的细节：每个要点下补一条，合计至少 3 条，并且来自不同要点。
- 人称、时态要转换正确，要有过渡衔接，语音语调要自然。
- 发音错误、不当停顿、自我纠正都算语言错误。说错了不要回头重说，也不要说 “Sorry”。
- 开口前停 1–2 秒。语速每分钟 100 词左右就够了，2 分钟大约 120–180 词，不必说满。

### 练习用分档参考（满分 9 分）

| 档次 | 分数 | 表现 |
|---|---|---|
| 一档 | 8–9 | 表格信息完整；补充 ≥3 条来自不同要点的细节；结构清楚，衔接自然；人称时态正确；语言错误很少，没有明显卡顿或自我纠正 |
| 二档 | 6–7 | 表格信息基本完整；补充 1–2 条细节；有少量错误或停顿，但不影响理解 |
| 三档 | 4–5 | 漏掉部分表格信息，基本没有补充；错误和停顿较多 |
| 四档 | 1–3 | 只说出零散信息，较难听懂 |

> 这是根据公开备考资料整理的练习参考，不是官方评分细则。

## 转述常用表达

- **开头**：The speaker tells us / shares / introduces / is talking about …
- **转述动词**：says, points out, explains, mentions, suggests doing, advises us to do, encourages us to do, reminds us to do
- **衔接**：First / To begin with → Besides / What's more / In addition → Finally / In the end；because, so, however, while, in contrast, for example
- **人称**：I → he / she（the speaker）；you → we / us
- **时态**：介绍和建议用一般现在时，经历和研究过程用一般过去时

## 题型信息来源

{sources}

## 重新生成

修改 `_build/content.py` 后运行 `python3 _build/build.py`。加 `--audio` 会重新合成音频，需要先 `pip install edge-tts imageio-ffmpeg`，并且能联网。加 `--pdf` 会重新打印 PDF，需要 Node.js 和 playwright（`npm i -g playwright && npx playwright install chromium`）。
"""


# ---------- practice page ----------

def page(durs):
    data = []
    for s in SETS:
        d = {k: s[k] for k in ("id", "slug", "topic_cn", "theme", "genre", "speaker", "pronoun",
                               "title", "opening", "rows", "answers", "pitfalls")}
        d["script"] = paras(s["script"])
        d["model"] = paras(s["model"])
        d["vocab"] = [list(v) for v in s["vocab"]]
        d["audio"] = f"audio/{s['slug']}.mp3"
        d["duration"] = durs.get(s["slug"], 0)
        d["words"] = words(s["script"])
        d["model_words"] = words(s["opening"] + " " + s["model"])
        data.append(d)
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    src = (HERE / "page_template.html").read_text(encoding="utf-8")
    src = src.replace("/*__DATA__*/null", blob)
    src = src.replace("<!--__SOURCES__-->", "".join(
        f'<li><a href="{html.escape(u)}" target="_blank" rel="noopener">{html.escape(t)}</a></li>'
        for t, u in SOURCES))
    return src


# ---------- print (PDF) ----------

def bold_md(text):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(text))


def print_passages():
    out = ['<section class="passages">']
    first_long = True
    for i, p in enumerate(PASSAGES, 1):
        cls = "passage"
        if len(p.split()) > 100 and first_long:  # the long passages start on a new page
            cls += " newpage"
            first_long = False
        body = "".join(f"<p>{html.escape(x)}</p>" for x in paras(p))
        out.append(f'<article class="{cls}"><h2>短文 {i}</h2><div class="en">{body}</div></article>')
    out.append("</section>")
    return "\n".join(out)


def print_student():
    def gaps(t):
        return re.sub(r"\[(\d)\]", r'<span class="blank">(\1)<span class="gap"></span></span>', html.escape(t))

    out = ['<section class="sheets">', '<header class="sheet-title">', f"<h1>{SHEET_TITLE}</h1>",
           *[f"<p>{bold_md(n)}</p>" for n in SHEET_NOTES], "</header>"]
    for s in SETS:
        rows = []
        for r in table_rows(s):
            items = [gaps(t) for t in r["table"]]
            body = items[0] if len(items) == 1 else "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
            rows.append(f'<tr><th scope="row">{html.escape(r["main"])}</th><td>{body}</td></tr>')
        out.append(
            f'<article class="set"><h2>第 {s["id"]} 套</h2>'
            f"<h3>{RECORD[0]}<span>{RECORD[1]}</span></h3><p class=\"instr\">{RECORD[2]}</p>"
            f'<table class="record en"><thead><tr><th colspan="2">{html.escape(s["title"])}</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table>'
            f"<h3>{RETELL[0]}<span>{RETELL[1]}</span></h3><p class=\"instr\">{RETELL[2]}</p>"
            f'<div class="rules"><div class="rule en">{html.escape(s["opening"])}</div>'
            + '<div class="rule"></div>' * 5 + "</div></article>")
    out.append("</section>")
    return "\n".join(out)


def print_doc(title, body):
    css = (HERE / "print.css").read_text(encoding="utf-8")
    return (f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
            f"<title>{html.escape(title)}</title><style>{css}</style></head><body>{body}</body></html>")


def make_pdfs():
    docs = {
        "passages-and-student-sheets": ("短文 1–5 · 学生版", print_passages() + print_student()),
        "student-sheets": (SHEET_TITLE, print_student()),
        "passages": ("短文 1–5", print_passages()),
    }
    PRINT_DIR.mkdir(exist_ok=True)
    PDF_DIR.mkdir(exist_ok=True)
    args = []
    for name, (title, body) in docs.items():
        src = PRINT_DIR / f"{name}.html"
        src.write_text(print_doc(title, body), encoding="utf-8")
        args += [str(src), str(PDF_DIR / f"{name}.pdf")]
    env = dict(os.environ)
    try:  # let node find a globally installed playwright
        root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True, check=True).stdout.strip()
        env["NODE_PATH"] = os.pathsep.join(p for p in (env.get("NODE_PATH"), root) if p)
    except (OSError, subprocess.CalledProcessError):
        pass
    subprocess.run(["node", str(HERE / "pdf.js"), *args], check=True, env=env)


# ---------- audio ----------

def duration_of(path):
    import imageio_ffmpeg
    r = subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-i", str(path)], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    return int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3])


async def synth_all():
    import certifi
    # edge-tts trusts only certifi's bundle; honour SSL_CERT_FILE (e.g. behind a TLS proxy).
    # Must happen before edge_tts is imported, because it builds its SSL context at import time.
    if os.environ.get("SSL_CERT_FILE"):
        certifi.where = lambda: os.environ["SSL_CERT_FILE"]
    import edge_tts
    AUDIO.mkdir(exist_ok=True)
    durs = {}
    for s in SETS:
        out = AUDIO / f"{s['slug']}.mp3"
        await edge_tts.Communicate(plain(s["script"]).strip(), s["voice"], rate=s["rate"]).save(str(out))
        durs[s["slug"]] = round(duration_of(out), 1)
        wpm = words(s["script"]) / durs[s["slug"]] * 60
        print(f"  {out.name}: {fmt_dur(durs[s['slug']])}, {wpm:.0f} wpm")
    DURATIONS.write_text(json.dumps(durs, indent=2) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio", action="store_true", help="re-synthesise the MP3 files")
    ap.add_argument("--pdf", action="store_true", help="print the PDF handouts")
    args = ap.parse_args()
    if args.audio:
        print("audio:")
        asyncio.run(synth_all())
    durs = load_durations()
    outputs = {
        "README.md": md_readme(durs),
        "passages.md": md_passages(),
        "student-sheets.md": md_student(),
        "teacher-key.md": md_teacher(durs),
        "sense-groups.md": md_sense(),
        "practice.html": page(durs),
    }
    for name, text in outputs.items():
        (ROOT / name).write_text(text.rstrip() + "\n", encoding="utf-8")
        print(f"wrote {name}")
    if args.pdf:
        print("pdf:")
        make_pdfs()


if __name__ == "__main__":
    main()
