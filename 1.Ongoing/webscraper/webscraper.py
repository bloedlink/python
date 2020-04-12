import requests
from bs4 import BeautifulSoup
import pprint

def readable(junk):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(junk)


res = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(res.text, 'html.parser')
links = (soup.select('.storylink'))
votes = (soup.select('.score'))


def filtered_page(links,votes):
    hn = []
    for i, item in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href')
        hn.append({'title':title,'href':href})
        points = votes[i].getText()
        readable(points)
    return hn

filtered_page(links,votes)