# Variable to reference the Python interpreter
PYTHON := python

.PHONY: footnote
footnote:
	@$(PYTHON) footnote.py

# Target rule for building PDF
pdf: index.qmd footnote
	quarto render --to pdf

latex: index.qmd footnote
	quarto render --to latex

# Remove generated files
.SILENT:
.PHONY: clean
clean:
	$(RM) -r .quarto .jupyter_cache *_cache *_files _freeze \
	contents/*bak.qmd publish/
