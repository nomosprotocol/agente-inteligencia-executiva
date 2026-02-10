import requests
from bs4 import BeautifulSoup
import feedparser

class NewsScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def scrape_g1(self):
        url = "https://g1.globo.com/"
        news_list = []
        try:
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            for item in soup.select('.feed-post-body')[:10]:
                title = item.select_one('.feed-post-link')
                summary = item.select_one('.feed-post-body-resumo')
                if title:
                    news_list.append({
                        'title': title.text.strip(),
                        'summary': summary.text.strip() if summary else "Sem resumo disponível",
                        'source': 'G1'
                    })
        except Exception as e:
            print(f"Erro ao raspar G1: {e}")
        return news_list

    def scrape_rss(self):
        url = "https://g1.globo.com/rss/g1/tecnologia/"
        news_list = []
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:10]:
                news_list.append({
                    'title': entry.title,
                    'summary': entry.summary if 'summary' in entry else "Sem resumo disponível",
                    'source': 'G1 Tecnologia (RSS)'
                })
        except Exception as e:
            print(f"Erro ao ler RSS: {e}")
        return news_list
