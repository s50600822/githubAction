from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


ops = webdriver.FirefoxOptions()
ops.headless=True
browser = webdriver.Firefox(options=ops)

browser.get('https://hoaphan.net')
print(browser.find_element(By.TAG_NAME, "body").text)

browser.quit()