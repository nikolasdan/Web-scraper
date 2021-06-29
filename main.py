import requests
from bs4 import BeautifulSoup

URL = "https://www.cel.ro/calculatoare-desktop/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find(class_="content-wrapper")
products = content.find_all(class_="product_data")

for data in products:
    title_prod = data.find(class_="productTitle")
    link_prod = data.find('a')['href']
    price_prod = data.find(class_="price")
    stoc_status = data.find(class_="info_stoc")
    print(title_prod.text)
    print(link_prod)
    print(price_prod.text + " lei")
    print(stoc_status.text)
    print("\n")
