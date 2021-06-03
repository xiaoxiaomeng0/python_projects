from selenium import webdriver

chrome_driver_path = "/Users/Kenny/Documents/Meng'coding/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://www.amazon.com/gp/product/B07Y2FKW71?pf_rd_r=G8NRYQS8TN7QV7NFHY2A&pf_rd_p=5ae2c7f8-e0c6-4f35-9071-dc3240e894a8&pd_rd_r=36b1b38d-a56f-42c9-838c-6398ea57b48e&pd_rd_w=llYc6&pd_rd_wg=iaQp6&ref_=pd_gw_unk")

price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)

# find element by name. The name here is the selector's attribute "name".
search_bar = driver.find_element_by_name("q")
print(search_bar) # it returns a selenium object.
print(search_bar.tag_name) # it returns a tag name, eg: input, p, a
print(search_bar.get_attribute("placeholder")) # it returns a particular attribute.

logo = driver.find_element_by_class_name("python-logo")
print(logo.size) # get the size of the logo.

document_link = driver.find_element_by_css_selector(".documentation-widget a")
print(document_link.text) # select the abchor tag within a particular class.

description = driver.find_element_by_xpath('//*[@id="feature-bullets"]/ul/li[1]/span')
print(description.text) # to get the xpath, right click the element to copy the xpath.

#driver.find_element_by_xpath() find a single one and driver.find_elements_by_xpath() find all of the elements. Same with all the method.

driver.quit()