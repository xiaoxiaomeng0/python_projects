from bs4 import BeautifulSoup
import requests
import re
from collections import deque

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# news_anchor_list = soup.select(selector=".storylink")
# news_score_list = soup.select(selector=".score")
# print(len(news_score_list))
# print(len(news_anchor_list))
# print(news_anchor_list)
# print(news_score_list)

url_to_title_and_score = {}
curr_url = ''
urls_to_process = deque()
for item in enumerate(soup.find_all(class_=re.compile("storylink|score"))):

    if not item['class']:
        continue
    
    if item['class'][0] == 'storylink':
        if urls_to_process:
            pass
        urls_to_process.append({'url': item['href'], 'title': item.getText()})
    elif item['class'][0] == 'score':
        if urls_to_process:
            curr_url_with_tile = urls_to_process.popleft()
            url_to_title_and_score[curr_url_with_tile['url']] = {'title': curr_url_with_tile['title']}
            url_to_title_and_score[curr_url_with_tile['url']]['score'] = item.getText()


    # if i % 2 == 0:
    #     if item['class'][0] == 'storylink':
    #         curr_url = item['href']
    #         url_to_title_and_score[curr_url] = {'title': item.getText()}
    # else:
    #     if curr_url in url_to_title_and_score and 'score' not in url_to_title_and_score[curr_url]:
    #         continue
    #     if item['class'][0] == 'score':
    #         url_to_title_and_score[curr_url]['score'] = item.getText()
    #     elif item['class'][0] == 'storylink':
    #         url_to_title_and_score[curr_url]['score'] = '0 points'
    #         curr_url = item['href']
    #         url_to_title_and_score[curr_url] = {'title': item.getText()}


    # if item['class'][0] == 'storylink':
    #     curr_url = item['href']
    #     url_to_title_and_score[curr_url] = {'title': item.getText()}
    # elif item['class'][0] == 'score':
    #     if curr_url in url_to_title_and_score and 'score' not in url_to_title_and_score[curr_url]:
    #         url_to_title_and_score[curr_url]['score'] = item.getText()

# print(url_to_title_and_score)

max_score_url = ""
max_score = -1

for url, content in url_to_title_and_score.items():
    print(content)
    score_point = int(content["score"].split()[0])
    content["score"] = score_point
    if content["score"] > max_score:
        max_score = content["score"]
        max_score_url = url
print(url_to_title_and_score)


# news_list = []

# for i in range(len(news_anchor_list)):
#     news_element_details = {"text": news_anchor_list[i].getText(),
#                             "link": news_anchor_list[i].get("href"),
#                             "score": news_score_list[i].getText()}
#     news_list.append(news_element_details)

# print(news_list)




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