
clean:
	@rm *.pdf
	@rm *.dvi -R
	@rm *.log -R
	@rm *.bbl -R
	@rm *.blg -R
	@rm *.toc -R
	@rm *.lof -R
	@rm *.lot -R

build:
	@latex dvro

bib:
	@bibtex dvro
	@latex dvro
	@latex dvro

pdf:
	@dvipdfm dvro.dvi

all:
	@make clean
	@make build
	@make bib
	@make pdf

