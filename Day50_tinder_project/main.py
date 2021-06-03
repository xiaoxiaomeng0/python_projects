from selenium import webdriver
import time
import os
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

load_dotenv()

chrome_driver_path = "/Users/Kenny/Documents/Meng'coding/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://tinder.com/"
driver.get(url)

time.sleep(2)
log_in = driver.find_element_by_xpath('//*[@id="o1286841894"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
time.sleep(2)
log_in.click()

time.sleep(2)
log_in_with_fb = driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
time.sleep(2)
log_in_with_fb.click()

base_window = driver.window_handles[1]
fb_login_window = driver.window_handles[-1]
driver.switch_to.window(fb_login_window)
print(driver.title)


email_name = driver.find_element_by_id("email")
email_name.send_keys("xiaoxiaomeng0@gmail.com")
email_pass = driver.find_element_by_id("pass")
email_pass.send_keys(os.environ.get("FACEBOOK_PASS"))
email_login = driver.find_element_by_name("login")
email_login.click()

driver.switch_to.window(base_window)
print(driver.title)

location_pop_up = driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div/div/div[3]/button[1]/span')
location_pop_up.click()
time.sleep(1)

notification_pop_up = driver.find_elements_by_xpath('//*[@id="o-441539182"]/div/div/div/div/div[3]/button[2]/span')
notification_pop_up.click()
time.sleep(1)

cookies_pop_up = driver.find_elements_by_xpath('//*[@id="o1286841894"]/div/div[2]/div/div/div[1]/button/span')
cookies_pop_up.click()
time.sleep(1)

for n in range(100):
    time.sleep(1)
    try:
        dislike = driver.find_elements_by_xpath('//*[@id="o1286841894"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button/span/svg/path')
        dislike.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)





# driver.close()