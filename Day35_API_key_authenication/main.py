import requests

parameters = {
    "lat": 33.661430,
    "lon": -95.556320,
    "exclude": "current,minutely,daily",
    "appid": "41626c2ac8d3235437a98606eb328704"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()["hourly"]
data_lists = data[:12]
condition_code = [data["weather"][0]["id"] for data in data_lists if data["weather"][0]["id"] < 700]

if condition_code:
    print("bring umbralla")