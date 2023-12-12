from bs4 import BeautifulSoup
import requests
import pandas as pd


r = requests.get('https://en.wikipedia.org/wiki/Web_scraping')

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.prettify())

images_list = []

images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})


df = pd.DataFrame(images_list)

df.to_csv('image_data.csv', index=False)
print("CSV file saved successfully!")

df = pd.read_csv('image_data.csv')


df['alt'].fillna("No description", inplace=True)

print(df.head(10))  

df.set_index('alt', inplace=True)
df.reset_index(inplace=True)
print(df.head(10)) 
print(df.tail(10)) 
