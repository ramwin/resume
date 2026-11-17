#!/usr/bin/env python3
"""把 README.md 渲染成适合打印的 A4 HTML，再由 Chrome 打印成 PDF。

用法::

    python3 export_pdf.py            # 生成 /tmp/resume_print.html
    python3 export_pdf.py -o x.pdf   # 直接调 Chrome 出 PDF

样式与站点的 sphinx 主题无关，单独控制：A4、窄边距、紧凑行距，
让 AI Agent 方向的长版简历也能压到 3 页以内。
"""

from __future__ import annotations

import argparse
import pathlib
import shutil
import subprocess
import tempfile

try:
    import markdown
except ModuleNotFoundError:  # pragma: no cover - 引导用户装依赖
    raise SystemExit(
        "缺少 markdown 模块。直接跑 `make pdf` 即可（会自动建 .venv-pdf），\n"
        "或手动: python3 -m venv .venv-pdf && .venv-pdf/bin/pip install markdown"
    )

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "README.md"


CSS = """
@page { size: A4; margin: 13mm 12mm 12mm 12mm; }
* { box-sizing: border-box; }
body {
  font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
  font-size: 9.8pt; line-height: 1.52; color: #1d2129; margin: 0;
}
h1 {
  font-size: 17pt; margin: 0 0 2mm; padding-bottom: 2mm;
  border-bottom: 2px solid #1d2129; letter-spacing: .5px;
}
h2 {
  font-size: 12pt; margin: 4.6mm 0 1.8mm; padding-left: 2.4mm;
  border-left: 3.5px solid #2f6feb; line-height: 1.3;
}
h3 { font-size: 10.4pt; margin: 3.2mm 0 1.2mm; color: #0f2b5b; }
blockquote {
  margin: 0 0 2mm; padding: 2mm 3mm; background: #f6f8fa;
  border-left: 3px solid #c8d1dc; color: #3d444d; font-size: 9.4pt;
}
blockquote p { margin: 0; }
p { margin: 1mm 0; }
ul, ol { margin: 1mm 0 1.4mm; padding-left: 5mm; }
li { margin: .5mm 0; }
li > ul { margin: .4mm 0; }
strong { color: #0b1b33; }
a { color: #1a56c4; text-decoration: none; }
table { width: 100%; border-collapse: collapse; margin: 1.4mm 0 2mm; font-size: 9.2pt; }
th, td { border: .4pt solid #d0d7de; padding: 1.1mm 1.8mm; vertical-align: top; text-align: left; }
td:first-child, th:first-child { white-space: nowrap; }
/* 表格按出现顺序定制: 1 基础信息 / 2 工作经历 / 3 插件 / 4 教育经历 */
table:nth-of-type(2) th:nth-child(1) { width: 17%; }
table:nth-of-type(2) th:nth-child(2) { width: 19%; }
table:nth-of-type(2) th:nth-child(3) { width: 12%; }
table:nth-of-type(2) th:nth-child(3), table:nth-of-type(2) td:nth-child(3) { white-space: nowrap; }
table:nth-of-type(2) th:nth-child(4) { width: 52%; }
table:nth-of-type(3) th:nth-child(1) { width: 30%; }
table:nth-of-type(3) td:nth-child(1) { white-space: normal; word-break: break-all; }
table:nth-of-type(4) th:nth-child(1) { width: 22%; }
th { background: #eef2f7; font-weight: 600; }
tr { page-break-inside: avoid; }
h1, h2, h3 { page-break-after: avoid; }
hr { border: none; border-top: .4pt solid #d0d7de; margin: 2mm 0; }
"""

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium-browser",
    "/usr/bin/chromium",
]


def render(md_text: str) -> str:
    body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>王祥 · AI Agent 工程 / AI 全栈</title>
<style>{CSS}</style></head><body>
{body}
</body></html>
"""


def find_chrome() -> str | None:
    for path in CHROME_CANDIDATES:
        if pathlib.Path(path).exists():
            return path
    return shutil.which("google-chrome") or shutil.which("chromium")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-o", "--output", help="输出 PDF 路径；省略则只生成 HTML")
    parser.add_argument("--html", default=str(pathlib.Path(tempfile.gettempdir()) / "resume_print.html"))
    args = parser.parse_args()

    md_text = SRC.read_text(encoding="utf-8")
    html_text = render(md_text)
    html_path = pathlib.Path(args.html)
    html_path.write_text(html_text, encoding="utf-8")
    print(f"html: {html_path}")

    if not args.output:
        return 0

    chrome = find_chrome()
    if not chrome:
        print("找不到 Chrome/Chromium，只能输出 HTML")
        return 1
    out = pathlib.Path(args.output).resolve()
    subprocess.run(
        [
            chrome,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={out}",
            html_path.resolve().as_uri(),
        ],
        check=True,
        capture_output=True,
    )
    print(f"pdf:  {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
