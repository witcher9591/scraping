from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
driver = webdriver.Firefox()

trip = 'https://webscraper.io/test-sites/e-commerce/allinone'
driver.get(trip)
search_box = driver.find_elements("xpath","//p[@class='title']/a")
print(search_box)
search_box.send_keys('lenovo')
search_box.send_keys(Keys.RETURN)  
driver.implicitly_wait(10) 
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
titles = soup.find_all('div', class_='biGQs _P fiohW alXOW NwcxK GzNcM ytVPx UTQMg RnEEZ ngXxk')
for title in titles:
    title_text = title.text.strip()
    print(title_text)
driver.quit()
