# B_R_R
# M_S_A_W

"""
We do some scraping based on Youtube Channel of Hitesh
He does not recommend to scrape public sites, due to ethics matters
We do look up Machine Learning in wikipedia, and extract only Table of Contents data

While printing out the table of contents, we can see some extra information,
such as journals, see also, references and so on...

We just want to print out just table of contents without extra info.
"""

from bs4 import BeautifulSoup
import lxml
import requests


req=requests.get("https://en.wikipedia.org/wiki/Machine_learning")
soup=BeautifulSoup(req.text, 'lxml')
no_extra=soup.select('.mw-headline')[:-6] # The last 6 headings are not necesary
for i in no_extra:
    print(i.text)

