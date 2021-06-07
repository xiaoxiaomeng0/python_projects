from selenium import webdriver
import time

chrome_driver_path = "/Users/Kenny/Documents/Meng'coding/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://docs.google.com/forms/d/e/1FAIpQLSc0LskDWYk-_Jn5EEaWBWFrESqD39gckmxK2Tn1qE1JA9vykQ/viewform?usp=sf_link"
driver.get(url)


class InsertSheet():
    def __init__(self, addresses, prices, links):
        self.addresses = addresses
        self.prices = prices
        self.links = links

    def fill_form(self):
        for i in range(len(self.addresses)):
            inputs = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
            inputs[0].send_keys(self.addresses[i])
            inputs[1].send_keys(self.prices[i])
            inputs[2].send_keys(self.links[i])
            submit = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
            submit.click()
            time.sleep(1)
            another_request = driver.find_element_by_css_selector(".freebirdFormviewerViewResponseLinksContainer a")
            another_request.click()
            time.sleep(1)

        driver.close()
