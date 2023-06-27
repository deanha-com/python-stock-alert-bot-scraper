import time
from selenium import webdriver
from threading import Timer
from selenium.webdriver.chrome.options import Options

keyword = "civic"
min_price = any
max_price = "1200"


chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome("./chromedriver", options=chrome_options)
start_url = "https://www.gumtree.com/search?search_category=cars&search_location=se10&q="+keyword+"&min_price=&max_price="+max_price
driver.get(start_url)

car = driver.find_element_by_css_selector(".listing-title").text
print(driver)
print(car)
driver.close()
driver.quit()