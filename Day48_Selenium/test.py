from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/Kenny/Documents/Meng'coding/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
button = driver.find_element_by_css_selector("button")


first_name.send_keys("Anna")
last_name.send_keys("Xie")
email.send_keys("annaxie652@gmail.com")
button.send_keys(Keys.ENTER)

