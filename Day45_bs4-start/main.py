from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
news_list = soup.find_all(class_=re.compile("storylink|score"))

map_list = []
max_score = 0
max_score_title = ""
max_score_url = ""
for item in news_list:
    if item["class"][0] == "storylink":
        if len(map_list) == 0:
            map_list.append({"url": item["href"], "title": item.string})
        else:
            if len(map_list[-1]) == 2:
                map_list[-1]["score"] = 0
            else:
                map_list.append({"url": item["href"], "title": item.string})
    else:
        if len(map_list[-1]) == 2:
            map_list[-1]["score"] = int(item.string.split()[0])
        if map_list[-1]["score"] > max_score:
            max_score = map_list[-1]["score"]
            max_score_url = map_list[-1]["title"]
            max_score_title = map_list[-1]["url"]
print(max_score)
print(max_score_title)
print(max_score_url)

# import lxml
#
#
# with open("website.html") as file:
#     web = file.read()
#     # print(web)
#
# soup = BeautifulSoup(web, "html.parser")
# # this method only the first.
# print(soup.h3)
# print(soup.h3.name)# get the name of the selector
# print(soup.h3.string) # get the content of the selector here.
#
# # find all the tags with the same selector name.
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# # only want the text of the anchor tags
# for tag in all_anchor_tags:
#     print(tag.getText()) # get the text only
#     print(tag.get("href")) # get any attribute.
#
# # to find a particular "id" or "class"
# heading = soup.find(name="h1", id="name")
# section_heading = soup.find(name="h3", class_="heading") # class keyword is a special keyword.
# print(heading)
# print(section_heading.get("class"))
#
# # use css selector to select
# company_url = soup.select_one(selector="p a")
# name = soup.select_one(selector="#name")
# heading_css = soup.select(".heading")
# print(name)