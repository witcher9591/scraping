from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Firefox()
url = 'https://ekantipur.com/'
driver.get(url)
start_time = time.time()
most_read_section = driver.find_element(By.CLASS_NAME, 'main-news')
articles_list = []

if most_read_section:
    news_articles = most_read_section.find_elements(By.TAG_NAME, 'article')

    for index, article in enumerate(news_articles):
        headline_element = article.find_element(By.TAG_NAME, 'a')
        headline = headline_element.text
        link = headline_element.get_attribute('href')
        
        summary_element = article.find_element(By.XPATH, './/p')  
        summary = summary_element.text
        
        article_data = {
            'headline': headline,
            'summary': summary,
            'link': link,
            'time':[],
            'writer':[],
            'writer url':[],
            'image':[],           
            'paragraphs': []  
        }

        original_window = driver.current_window_handle

        driver.execute_script("window.open('');")  
        driver.switch_to.window(driver.window_handles[1])  

        driver.get(link)
        try:
            most_section = driver.find_element(By.CSS_SELECTOR, 'article.normal')
            p_elements = most_section.find_elements(By.TAG_NAME, 'p') 

            for p_element in p_elements:
                paragraph_text = p_element.text
                article_data['paragraphs'].append(paragraph_text)

        except Exception as e:
            print(f"Error: {e}")
            pass
        try:
            time_element = driver.find_element(By.CSS_SELECTOR, 'time[style="display:inline-block"]')
            nepali_date = time_element.text
            article_data['time'].append(nepali_date)
   
            print("Nepali Date:", nepali_date)
        except Exception as e:
            print(f"Error: {e}")
            pass

        
        
        try:
            author_element = driver.find_element(By.CSS_SELECTOR, 'span.author a')
            author_name = author_element.text
            author_link = author_element.get_attribute('href')
            article_data['writer'].append(author_name)
            article_data['writer url'].append(author_link)
            
            
            
            print("Author Name:", author_name)
            print("Author Link:", author_link)
        except Exception as e:
            print(f"Error: {e}")
        pass
                
        try:
            image_element = driver.find_element(By.CLASS_NAME, 'image-caption')
            image_url = image_element.get_attribute('data-path')
            base_url="https://assets-cdn-api.kantipurdaily.com/thumb.php?src=https://assets-cdn.kantipurdaily.com/uploads/source/"
            full_url = base_url + image_url
            article_data['image'].append(full_url)
   
            print("Image URL:", image_url)
        except Exception as e:
            print(f"Error: {e}")
        pass



        articles_list.append(article_data)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time} seconds")
        driver.close()  
        driver.switch_to.window(original_window)  

        print("Headline:", headline)
        print("Summary:", summary)
        print("Link:", link)
        print("time:", article_data['time']) 
        print("Paragraphs:", article_data['paragraphs']) 
        print("\n")

with open('ekantipur_articles4.json', 'w', encoding='utf-8') as json_file:
    json.dump(articles_list, json_file, ensure_ascii=False, indent=4)

driver.quit()
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time} seconds")