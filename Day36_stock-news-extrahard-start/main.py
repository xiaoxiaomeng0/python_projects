import requests
import os
from dotenv import load_dotenv
import datetime as dt
import smtplib
from twilio.rest import Client

load_dotenv()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_EMAIL = "annaxie652@gmail.com"
PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)



stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("STOCK_API_KEY")
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
stock_data = stock_data["Time Series (Daily)"]
print(stock_data)

today = dt.date.today()
yesterday = str(today - dt.timedelta(days=1))
the_day_before_yesterday = str(today - dt.timedelta(days=2))
yesterday_price = float(stock_data[yesterday]["4. close"])
before_yesterday_price = float(stock_data[the_day_before_yesterday]["4. close"])

difference = abs(yesterday_price - before_yesterday_price) / yesterday_price

news_parameters = {
    "q": COMPANY_NAME,
    "from": str(today),
    "sortBy": "popularity",
    "apiKey": os.environ.get("NEWS_API_KEY")
}

print(news_parameters["q"])
if difference > 0.001:
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]
    print(news_data)
    for news in news_data:
        headline = news["title"]
        brief = news["description"]
        if yesterday_price >= before_yesterday_price:
            message = client.messages.create(
                body=f"TSLA: 🔺{round(difference * 100)}%\n"
                     f"Headline: {headline}\n"
                     f"Brief: {brief}",
                from_="+14075054806",
                to="+18144415603"
            )
        else:
            message = client.messages.create(
                body=f"TSLA: 🔻{round(difference * 100)}%\n"
                     f"Headline: {headline}\n"
                     f"Brief: {brief}",
                from_="+14075054806",
                to="+18144415603"
            )

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 




## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

