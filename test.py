from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.parse import urljoin

def extract_card_details(soup):
    print("extract_card_details function calles\n")
    card_details = []
    card_bodies = soup.find_all('div', class_='card-body')
    for card_body in card_bodies:
        img = card_body.find('img')
        if img:
            img_src = img.get('src')
            price = card_body.find('h4', class_='price')
            if price:
                price_text = price.text.strip()
                card_details.append({"Image Source": img_src, "Price": price_text})
    df_card_details = pd.DataFrame(card_details)
    df_card_details.to_csv('pricenimg.csv', index=False)
    print("CSV file saved successfully!")
    
   

def process_data(file_path):
    print("process_data function called\n")
    data = pd.read_csv(file_path)

    column_list = ['Phones', 'Laptops', 'Tablets']
    df = pd.DataFrame(column_list)
    print("printing df\n",df)

    filtered_data = data[(data['text'] == 'Phones') | (data['text'] == 'Computers')]
    print('Filtered data printing \n', filtered_data)

    categories = ['Phones', 'Computers']
    for category in categories:
        if category in filtered_data['text'].values:
            href_value = filtered_data.loc[filtered_data['text'] == category, 'href'].values[0]
            subcategory = 'Touch' if category == 'Phones' else 'Tablets' if category == 'Computers' else 'Laptops'

            full_url = urljoin('https://webscraper.io/', href_value + '/' + subcategory)
            response = requests.get(full_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                card_details = [{"Image Source": img.get('src'), "Price": price.text.strip()}
                                for card_body in soup.find_all('div', class_='card-body')
                                if (img := card_body.find('img')) and (price := card_body.find('h4', class_='price'))]

                df_card_details = pd.DataFrame(card_details)
                df_card_details.to_csv(f'{category.lower()}priceimg.csv', index=False)
                print(f"CSV file for {category} saved successfully!")
                print(f"Title of {full_url}: {soup.title.text}")

            else:
                print(f"Failed to retrieve {full_url}")

    if all(category not in filtered_data['text'].values for category in categories):
        print("No 'Phones' or 'Computers' found in the 'text' column.")
 
 
def product_scrape(url):
    print("product scrape is called")
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        product_prices = soup.find_all('h4', class_='float-end price card-title pull-right')
        product_description = soup.find_all('p', class_='description card-text')
        product_reviews = soup.find_all('p', class_='float-end review-count')
        product_titles=soup.find_all('a',class_='title')

     
        min_length = min(len(product_prices), len(product_titles), len(product_reviews),len(product_description))
        product_list=[]
        for i in range(min_length):
            title = product_titles[i].get_text(strip=True)
            price = product_prices[i].get_text(strip=True)
            review = product_reviews[i].get_text(strip=True)
            description=product_description[i].get_text(strip=True)
            
            
            print(f"Product: {title}, Price: {price}, Reviews: {review},Description:{description}")
            product_list.append({"title": title, "price": price,"review":review,"description":description})
            
            df_products = pd.DataFrame(product_list)
            df_products.to_csv('productsreviewsname.csv', index=False)
            
    else:
        print("Failed to fetch the page")

def scrape_and_save(url):
    print("Scrape and save function calles\n")
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Scraping images
    images_list = []    
    images = soup.select('img')
    for image in images:
        src = image.get('src')
        alt = image.get('alt')
        images_list.append({"src": src, "alt": alt})
    df_images = pd.DataFrame(images_list)
    print("Printing df image list", df_images)

    # Scraping navigation items
    nav_items = soup.find_all('li', class_='nav-item')
    links_list = []
    for nav_item in nav_items:
        link = nav_item.find('a')
        if link:
            href = link.get('href')
            text = link.get_text(strip=True)
            links_list.append({"href": href, "text": text})
    df_links = pd.DataFrame(links_list)
    df_links.to_csv('links.csv', index=False)
    print("Printing href or list with class nav_item", df_links)

   
    file_path = 'links.csv'
 #   extract_card_details(soup)
  #  process_data(file_path)
    product_scrape("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
   
if __name__ == '__main__':
    scrape_and_save("https://webscraper.io/test-sites/e-commerce/allinone")