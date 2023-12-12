from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('https://ekantipur.com')
search_bar = driver.find_elements("xpath","//*[@id='wrapper']")
for search in search_bar:
    print(search.text)



imagess =  driver.find_elements("xpath","/html/body/div[7]/div[3]/div[2]/div[1]/main/section[7]/div/div[2]/article[5]/div[1]/figure/a/img")
images_dict = {image: image.get_attribute("src") for image in imagess}
for  images,src in images_dict.items():
    print("Image:", images.text)
    print("Source:\n", src)
driver.quit()
# image_element = driver.find_elements('xpath','//img[@src="/html/body/div[7]/div[3]/div[2]/div[1]/main/section[7]/div/div[2]/article[5]/div[1]/figure/a/img"]')

# image_source= image_element.get_attribute('src')
# print("Image Source\n",image_source)
