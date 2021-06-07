from bs4 import BeautifulSoup
import requests
from google_form import InsertSheet


url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    # "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=url, headers=headers)
zillow_page = response.text
# print(zillow_page)

soup = BeautifulSoup(zillow_page, "html.parser")

price_list = soup.find_all(class_="list-card-price")
price_only = [price.getText().split("/")[0] for price in price_list]

address_list = soup.select(selector=".list-card-info a")
address_only = [address.getText().split(" | ")[-1] for address in address_list]
address_link = []
for address in address_list:
    address = address.get("href")
    if address[0:1] == "/b":
        address = "https://www.zillow.com" + address
    address_link.append(address)


new_sheet = InsertSheet(address_only, price_only, address_link)
new_sheet.fill_form()
