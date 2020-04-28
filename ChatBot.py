from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# creating a instance of Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
# method to navigate to a given page
driver.get("https://www.youtube.com/?hl=pt&gl=BR")
#driver.get("http://www.python.org")

#assert "Youtube" in driver.title

#elem = driver.find_element_by_name("q")
elem = driver.find_element_by_id("search")
search = driver.find_element_by_css_selector("ytd-masthead form#search-form input#search")
search.click()

search.send_keys("mkbhd")
search.submit()

delay(5)

#elem.click()
#elem.clear()
#elem.send_keys("mkbhd")
#elem.send_keys(Keys.RETURN)

assert "No result found." not in driver.page_source
driver.close()