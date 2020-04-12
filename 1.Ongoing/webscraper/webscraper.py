import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(res.content,'html.parser')
title = soup.select('.storylink')
votes = soup.select('.score')

def webscraper(title,votes):
    for indx,item in enumerate(title):
        links = title[indx].getText()
        print(links)
        points = votes[indx].getText()
        print (points)
        points = votes.getText()
        print(points)
webscraper(title,votes)
