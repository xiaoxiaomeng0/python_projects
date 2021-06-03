from selenium import webdriver
import time

chrome_driver_path = "/Users/Kenny/Documents/Meng'coding/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path, )

url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(url)

cookie_number = driver.find_element_by_id("cookies")
cookie = driver.find_element_by_id("bigCookie")

responded = False
while not responded:
    if cookie_number.text:
        responded = True

cookie_number = cookie_number.text.split()[0]

while True:

    cookie.click()
    tools = driver.find_elements_by_class_name("product unlocked enabled")
    time.sleep(1)
    print(tools)




