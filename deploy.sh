git clone https://github.com/timothycrosley/attila.git
pelican-themes -i attilla
rm -rf attila
pelican
ghp-import output -b gh-pages
git push origin gh-pages
