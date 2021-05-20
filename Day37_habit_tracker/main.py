import requests
from dotenv import load_dotenv
import os
import datetime as dt

load_dotenv()

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = "xiaoxiaomeng0"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"

today = dt.date.today()
separator = ""
today = separator.join((str(today).split("-")))
# date.strftime is used to format the date eg. (today.strftime("%Y%m%d")


pixel_config = {
    "date": today,
    "quantity": "1.00"
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

put_pixel_endpoint = f"{post_pixel_endpoint}/{today}"

update_pixel = {
    "quantity": "5.00"
}

# response = requests.put(url=put_pixel_endpoint, json=update_pixel, headers=headers)
# print(response.text)

delete_pixel_endpoint = put_pixel_endpoint

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)