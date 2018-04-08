import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site
        self.links = []
        self.headlines = []

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all('a'):
            url = tag.get('href')
            if url is None:
                continue
            if 'html' in url:
                self.links.append(url)
        return self

    def scrape_detail(self):
        for url in self.links:
            sp = BeautifulSoup(url, 'html5lib')
            article = sp.find('article')
            if article is None:
                continue
            else:
                self.headlines.append(article)
        print(self.headlines)


if __name__ == '__main__':
    news = 'https://news.google.com/'
    Scraper(news).scrape().scrape_detail()
