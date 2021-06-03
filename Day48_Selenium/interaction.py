from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/Kenny/Documents/Meng'coding/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

count = driver.find_element_by_css_selector("#articlecount a")
count.click() # click the anchor tag.

#another way of click the anchor tag
all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()

#type text in the search bar
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)




driver.quit()
