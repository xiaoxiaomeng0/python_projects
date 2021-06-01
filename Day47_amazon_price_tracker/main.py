from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

LOWEST_PRICE = 600
my_email = "annaxie652@gmail.com"
password = os.environ.get("PASSWORD")

url = "https://www.amazon.com/Roborock-Navigation-Selective-Cleaning-Powerful/dp/B07ZVCPDB4/ref=sr_1_2_sspa?dchild=1&keywords=roborock+s5&qid=1622575343&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyT09WVElCVjc0NVA0JmVuY3J5cHRlZElkPUEwOTA1NTI2TUYwU1lQVDNNN1IzJmVuY3J5cHRlZEFkSWQ9QTAxNTU3NDFHUjNMWTZVSzJJTEomd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

headers = {
    "content-encoding": "gzip",
    # "content-length": "2457",
    "content-type": "text/html",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
price = float(soup.find(name="span", id="priceblock_ourprice").string[1:])
title = soup.find(name="span", id="productTitle").string.strip()

if price < LOWEST_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Low price alert\n\n {title}\nCurrent Price: ${price}\nURL: {url}"
        )