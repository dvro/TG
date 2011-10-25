

clean:
	@rm *.pdf
	@rm *.log -R
	@rm *.bbl -R
	@rm *.blg -R
	@rm *.toc -R
	@rm *.lof -R
	@rm *.lot -R
	@rm *.dvi -R

build:
	@latex dvro

bib:
	@bibtex dvro
	@latex dvro
	@latex dvro

pdf:
	@pdflatex dvro.tex

all:
	clean build bib pdf
