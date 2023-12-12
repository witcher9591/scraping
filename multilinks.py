from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

url = 'https://www.dcnepal.com/'

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get(url)

breaking_news_divs = driver.find_elements(By.CLASS_NAME, 'breaking__news')

new_list=[]
if breaking_news_divs:
    for div in breaking_news_divs:
        img_tag = div.find_element(By.TAG_NAME, 'img')
        title_tag = div.find_element(By.CSS_SELECTOR, 'a.title')

        img_src = img_tag.get_attribute('src')
        img_alt = img_tag.get_attribute('alt')

        img_src_text = img_src.strip() if img_src else "No image source found"
        img_alt_text = img_alt.strip() if img_alt else "No alt text found"

        news_title = title_tag.text.strip()
        new_list.append({"news_title":news_title,"image":img_src_text,"img_alt":img_alt_text})
        df_newsdetails=pd.DataFrame(new_list)
        df_newsdetails.to_csv("news",index=False)
        print("saved")

        print("News Title:", news_title)
        print("Image Source:", img_src_text)
        print("Alt Text:", img_alt_text)
else:
    print("Divs with class 'breaking__news' not found")

driver.quit()
