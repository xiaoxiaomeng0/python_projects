from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text

soup = BeautifulSoup(content, "html.parser")
h3 = soup.find_all(name="h3", class_="jsx-4245974604")
print(h3)
# Website changed. couldn't be able to continue the challenge.