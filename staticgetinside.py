import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.dcnepal.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
data_list = []

most_readed = soup.find('div', class_='most--readed')

if most_readed:
     # for article in most_readed:
    #     article_data={}

    news_articles = most_readed.find_all('div', class_='col--news')
   
    for article in news_articles:
        article_data = {}

        headline = article.find('a', class_='title')

        if headline:
            headline_text = headline.text.strip()
            article_url = headline['href']
            #  time_elem = article.find('span')
            # if time_elem:

            new_response = requests.get(article_url)
            article_soup = BeautifulSoup(new_response.content, 'html.parser')
            time_elem = article.find('span')
            if time_elem:
                time = time_elem.text.strip()
            else:
                time = "Publication time not found"
            article_content = article_soup.find('div', class_='news-content-area')
            paragraphs = article_content.find_next_sibling('p')

            # if article_content:
            #     first_paragraph = article_content.find('p')
            #     if first_paragraph:
            #         content_text = first_paragraph.text.strip()
            #     else:
            #   content_text = "No paragraph found"
            # else:
            #     content_text = "Content not f

            # if article_content:
                
                # paragraph_texts = []
 
                # for paragraph in paragraphs:
                # paragraph_text = paragraph.text.strip()
    
                #  paragraph_texts.append(paragraph_text)

                # content_text = '\n'.join(paragraph_texts)
                
                
                
                
                
                
            paragraphs = article_content.find_all('p')
            content_text = '\n'.join(paragraph.text.strip() for paragraph in paragraphs)
            # else:
            # content_text = "Content not found"

            article_data['Headline'] = headline_text
            article_data['URL'] = article_url
            article_data['Publication Time'] = time
            article_data['Content'] = content_text
            data_list.append(article_data)

df = pd.DataFrame(data_list)

csv_file = 'articles_data.csv'
df.to_csv(csv_file, index=False, encoding='utf-8')

print(f"Data saved to {csv_file}")
