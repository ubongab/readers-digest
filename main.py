import requests
from bs4 import BeautifulSoup

class RDScraper:
    BASE_URL = 'https://www.readersdigest.co.uk/'
    category = {'money':'money', 'inspire':'inspire', 'lifestyle':'lifestyle',
                'food-drink':'food-drink'}

    def __init__(self,category):
        self.news = []
        self.parse_page(self.category[category])

    def get_page(self,url):
        r = requests.get(url)
        return BeautifulSoup(r.text, 'html.parser')

    def parse_page(self,category):
        self.urls = [f"{self.BASE_URL}{category}"] +\
        [f"{self.BASE_URL}{category}?page={i}" for i in range(2,4)]
        for url in self.urls:
            soup = self.get_page(url)
            articles = soup.select('article')
            for art in articles:
                data = {}
                data['title'] = art.select_one('h2 > a').text.strip()
                data['link'] = art.select_one('h2 > a').attrs['href']
                data['tag'] = art.select_one("p.section > a ").text
                self.news.append(data)
        # print(self.news)

s = RDScraper('money')
print([x['title'] for x in s.news])
print(len(s.news))
