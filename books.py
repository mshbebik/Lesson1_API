import requests
import json
from bs4 import BeautifulStoneSoup



def books():
    name = input("Введіть назву ключового слова:")
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={name}+intitle:keyes&key=AIzaSyCE1fuJ62Yr3qi_6xKcNt7cmgUh_WxXHA8')
    data = json.loads(response.text)
    for i in data["items"]:
        for a in i["volumeInfo"]:
            print(a["title"], a["subtitle"], a["authors"])
books()
