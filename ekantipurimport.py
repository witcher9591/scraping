from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Firefox()
url = 'https://ekantipur.com/'
driver.get(url)


most_read_section = driver.find_element(By.CLASS_NAME, 'main-news')
articles_list = []

if most_read_section:
    news_articles = most_read_section.find_elements(By.TAG_NAME, 'article')

    for article in news_articles:
        headline_element = article.find_element(By.TAG_NAME, 'a')
        headline = headline_element.text
        link = headline_element.get_attribute('href')
        
        summary_element = article.find_element(By.XPATH, './/p')  
        summary = summary_element.text
        
        driver.get(link)
        most_section = driver.find_element(By.CLASS_NAME, 'description.current-news-block.portrait')
        p_elements = most_section.find_elements(By.CSS_SELECTOR, "[style='font-size: 1.041em !important;']")

        article_data = {
            'headline': headline,
            'summary': summary,
            'link': link,
            'paragraphs': []  
        }

        for p_element in p_elements:
            paragraph_text = p_element.text
            article_data['paragraphs'].append(paragraph_text)

            print("Paragraph:", paragraph_text)
            print("\n")

        articles_list.append(article_data)

        print("Headline:", headline)
        print("Summary:", summary)
        print("Link:", link)
        print("\n")

with open('ekantipur_articles2.json', 'w', encoding='utf-8') as json_file:
    json.dump(articles_list, json_file, ensure_ascii=False, indent=4)

driver.quit()
