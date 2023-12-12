import requests
from bs4 import BeautifulSoup

url = 'https://www.tripadvisor.com/Tourism-g293889-Nepal-Vacations.html'

response = requests.get(url, headers={'User-Agent': "Chrome/91.0.4472.124"})
soup = BeautifulSoup(response.content, 'lxml')


tourism_info = soup.find_all('div', class_='IDaDx')
for info in tourism_info:
    print(info.text)
