git clone https://github.com/timothycrosley/attila.git
venv/bin/pelican-themes -i attila
rm -rf attila
venv/bin/pelican
venv/bin/ghp-import output -b gh-pages
git push origin gh-pages
