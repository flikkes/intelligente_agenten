from bs4 import BeautifulSoup
import re
import requests

def crawlCategories():
    url = 'https://zeit.de/index'
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, features="html.parser")
    ressorts = soup.find('ul', class_='nav__ressorts-list').findAll('li')
    categories = []

    for ressort in ressorts:
        for ul in ressort.findAll('ul'):
            ul.decompose()
        span = ressort.find('span')
        a = ressort.find('a')
        if span is not None:
            categories.append({'name':span.string, 'url':a.attrs.get('href')})
    return categories

def crawlTeasers(url):
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, features="html.parser")
    articles = soup.findAll('article')
    teasers = []
    for article in articles:
        h3 = article.find('h3')
        titleParts = h3.findAll('span')
        title = titleParts[len(titleParts)-1]
        p = article.find('p')
        if p is not None and title is not None:
            teasers.append({'title':title.string, 'text':p.string})
    return teasers

categories = crawlCategories()
print(categories)
print(crawlTeasers(categories[0]['url']))
