import requests
from bs4 import BeautifulSoup

url = 'https://www.dcnepal.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

news_articles = soup.find_all('div', class_='col--news')
for article in news_articles:
    headline = article.find('a', class_='title')
    if headline:
        headline_text = headline.text.strip()
        article_url = headline['href']
        time_elem = article.find('span')
        if time_elem:
            time = time_elem.text.strip()
            print(f"Headline: {headline_text}")
            print(f"URL: {article_url}")
            print(f"Publication Time: {time}")
            print()
        else:
            print("Publication time not found")
