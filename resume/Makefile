all:
	pdflatex resume.tex
	cp resume.pdf Caleb-Adams-CV.pdf
	pdflatex 2page.tex
	cp 2page.pdf Caleb-Adams-2page-Resume.pdf
	pdflatex 01-2023cv.tex
	cp 01-2023cv.tex Caleb-Adams-short-cv-01-2023.pdf
cv:
	pdflatex resume.tex
	cp resume.pdf Caleb-Adams-CV.pdf
2page:
	pdflatex 2page.tex
	cp 2page.pdf Caleb-Adams-2page-Resume.pdf
clean:
	rm -f *~
	rm -f *.aux
	rm -f *.log
	# rm -f *.pdf
	rm -f *.out
