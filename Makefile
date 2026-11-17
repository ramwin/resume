# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# 简历 PDF 文件名(投递用), make pdf 会覆盖同名文件
PDF_NAME      = 王祥的简历_AI_Agent_上海交通大学
# PDF 只依赖 markdown, 用一个独立的小 venv, 不污染系统 python
PDF_VENV      = .venv-pdf

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# 内容定稿后再跑: README.md -> A4 打印版 PDF(需要本机有 Chrome/Chromium)
.PHONY: pdf
pdf:
	@test -d $(PDF_VENV) || python3 -m venv $(PDF_VENV)
	@$(PDF_VENV)/bin/python -c "import markdown" 2>/dev/null || $(PDF_VENV)/bin/pip install -q markdown
	$(PDF_VENV)/bin/python export_pdf.py -o "$(PDF_NAME).pdf"

.PHONY: help pdf Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
