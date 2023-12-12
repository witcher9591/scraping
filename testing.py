import requests
from bs4 import BeautifulSoup
from googlesearch import search

def search_keywords(keyword, num_results=1):
    try:
        search_results = list(search(keyword, stop=num_results))
        return search_results
    except Exception as e:
        print("An error occurred:", str(e))
        return None

search_keyword = input("Enter a Keyword to Search : ")
results = search_keywords(search_keyword, num_results=1)
print(results)
