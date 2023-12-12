import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 

driver = webdriver.Firefox()
url = 'https://ekantipur.com/'
driver.get(url)

wait = WebDriverWait(driver, 10)  

try:
    main_section = wait.until(EC.presence_of_element_located((By.ID, 'wrapper')))
    date_time = main_section.find_element(By.CSS_SELECTOR, '.todays-date time')
    nepali_date = date_time.text
    print("Nepali Date:", nepali_date)

    articles = main_section.find_elements(By.CLASS_NAME, 'normal')
    articles_list = []

    for article in articles:
        try:
            image_title = article.find_element(By.TAG_NAME, 'a').text
            summary = article.find_element(By.TAG_NAME, 'p').text
            url = article.find_element(By.TAG_NAME, 'a').get_attribute('href')

            article_info = {
                "Image Title": image_title,
                "Summary": summary,
                "URL": url
            }

            articles_list.append(article_info)
        except NoSuchElementException as e:
            print("Some elements not found within 'normal' class:", e)

    for article_info in articles_list:
        print("Image Title:", article_info['Image Title'])
        print("Summary:", article_info['Summary'])
        print("URL:", article_info['URL'])
        print("\n")

    # Saving data to a JSON file
    with open('extracted_data.json', 'w') as json_file:
        json.dump(articles_list, json_file, indent=4)

except NoSuchElementException as e:
    print("Main section or date time element not found:", e)

finally:
    driver.quit()
