import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
 

driver = webdriver.Firefox()
url = 'https://www.dcnepal.com/'
driver.get(url)

data_list = []  

most_readed = driver.find_element(By.CLASS_NAME, 'most--readed')
if most_readed:
    news_articles = most_readed.find_elements(By.CLASS_NAME, 'col--news')
    for article in news_articles:
        article_data = {} 
        
        headline = article.find_element(By.CLASS_NAME, 'title')
        if headline:
            headline_text = headline.text.strip()
            article_url = headline.get_attribute('href')

           
            driver.get(article_url)
            article_soup = BeautifulSoup(driver.page_source, 'html.parser')

            time_elem = article_soup.find('time', class_='updated')
            if time_elem:
                time = time_elem.text.strip()
            else:
                time = "Publication time not found"

          
            article_content = article_soup.find('div', class_='news-content-area')
            if article_content:
                paragraphs = article_content.find_all('p')
                content_text = '\n'.join(paragraph.text.strip() for paragraph in paragraphs)
            else:
                content_text = "Content not found"

           
            article_data['Headline'] = headline_text
            article_data['URL'] = article_url
            article_data['Publication Time'] = time
            article_data['Content'] = content_text
            
            data_list.append(article_data)

driver.quit()
csv_file = 'articles_data.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Headline', 'URL', 'Publication Time', 'Content']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for article_data in data_list:
        writer.writerow(article_data)

print(f"Data saved to {csv_file}")
