from selenium import webdriver

chrome_driver_path = "/Users/Kenny/Documents/Meng'coding/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://www.python.org/"
driver.get(url)

date_list = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')
date_list_text = [date.text for date in date_list]

events = {}
for i in range(len(date_list_text)):
    date = date_list_text[i].split("\n")[0]
    event_name = date_list_text[i].split("\n")[1]
    events[i] = {
        "time": date,
        "name": event_name,
    }

print(events)

driver.quit()
