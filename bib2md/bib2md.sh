#! /bin/bash
#
# Based on http://jmbarney.dyndns.org/?/linux/bib2mkd/

shopt -s expand_aliases

PREPRINT=ajw_preprint.bib
ARTICLES=ajw_article.bib 
CHAPTERS=ajw_book_chapters.bib  
PROCEEDINGS=ajw_proceedings.bib
PATENTS=ajw_patent.bib

alias bib2html='bibtex2html -noabstract -nokeys -nobibsource -nokeywords -d \
                -r -nodoc -noheader -o - -nofooter'
alias html2md='pandoc --normalize -S --reference-links -f html -t markdown'

HTML=tmp.html
MD=pubs.md

if [ -f $MD ]; then rm $MD; fi
touch $MD

echo '---' >> $MD
echo 'layout: page' >> $MD
echo 'title: "Publications"' >> $MD
echo 'date: 2011-12-08 17:30' >> $MD
echo 'comments: false' >> $MD
echo 'sharing: true' >> $MD
echo 'footer: true' >> $MD
echo '---' >> $MD
echo '' >> $MD


echo '### Preprints ###' >> $MD
echo '' >> $MD
bib2html $PREPRINT > $HTML
html2md $HTML >> $MD
echo '' >> $MD

echo '### Journal Papers ###' >> $MD
echo '' >> $MD
bib2html $ARTICLES > $HTML
html2md $HTML >> $MD
echo '' >> $MD

echo '### Conference Papers ###' >> $MD
echo '' >> $MD
bib2html $PROCEEDINGS > $HTML
html2md $HTML >> $MD
echo '' >> $MD

echo '### Book Chapters ###' >> $MD
echo '' >> $MD
bib2html $CHAPTERS > $HTML
html2md $HTML >> $MD
echo '' >> $MD

echo '### Patents ###' >> $MD
echo '' >> $MD
bib2html $PATENTS > $HTML
html2md $HTML >> $MD
echo '' >> $MD

echo '[My Google scholar profile](http://scholar.google.com/citations?user=jkHEZuoAAAAJ)' >> $MD
python fix.py $MD

cp $MD ~/projects/octopress/source/Publications/index.markdown
