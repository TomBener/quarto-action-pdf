# A variable listing all *.md files
QMD_FILES := $(filter-out %-bak.qmd,$(wildcard contents/[0-9]*.md))
# Convert the .md file names to bak.qmd file names
BAK_FILES := $(patsubst %.md,%-bak.qmd,$(QMD_FILES))

%-bak.qmd: %.md
	@perl -0777 -pe ' \
	  s/\s*\[@\].*?[\]\)]//g; \
	' $< > $@

# Variable to reference the Python interpreter
PYTHON := python

.PHONY: footnote
footnote:
	@$(PYTHON) footnote.py

# Target rule for building PDF
pdf: index.qmd $(BAK_FILES) footnote
	quarto render --to pdf

# Remove generated files
.SILENT:
.PHONY: clean
clean:
	$(RM) -r .quarto .jupyter_cache *_cache *_files _freeze \
	contents/*bak.qmd publish/
