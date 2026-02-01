import requests
from bs4 import BeautifulSoup
import json

class NewsScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def scrape_g1(self):
        """Scrapes news from G1 (Brazilian news)"""
        url = "https://g1.globo.com/"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            news_list = []
            # Find news items
            items = soup.find_all('div', class_='feed-post-body')
            
            for item in items[:10]:  # Limit to 10 items
                title_tag = item.find('a', class_='feed-post-link')
                summary_tag = item.find('div', class_='feed-post-body-resumo')
                
                if title_tag:
                    title = title_tag.get_text().strip()
                    link = title_tag.get('href')
                    summary = summary_tag.get_text().strip() if summary_tag else "Sem resumo disponível."
                    
                    news_list.append({
                        'title': title,
                        'link': link,
                        'summary': summary,
                        'source': 'G1'
                    })
            return news_list
        except Exception as e:
            print(f"Erro ao raspar G1: {e}")
            return []

    def scrape_rss(self, url="https://g1.globo.com/rss/g1/"):
        """Parses RSS feed for news"""
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, features="xml")
            
            news_list = []
            items = soup.find_all('item')
            
            for item in items[:10]:
                title = item.title.text if item.title else "Sem título"
                link = item.link.text if item.link else ""
                description = item.description.text if item.description else "Sem descrição"
                # Clean description (remove HTML tags if any)
                clean_description = BeautifulSoup(description, "html.parser").get_text()
                
                news_list.append({
                    'title': title,
                    'link': link,
                    'summary': clean_description,
                    'source': 'RSS Feed'
                })
            return news_list
        except Exception as e:
            print(f"Erro ao ler RSS: {e}")
            return []

if __name__ == "__main__":
    scraper = NewsScraper()
    print("Testando G1...")
    print(json.dumps(scraper.scrape_g1()[:2], indent=2, ensure_ascii=False))
    print("\nTestando Google News...")
    print(json.dumps(scraper.scrape_google_news("IA")[:2], indent=2, ensure_ascii=False))
