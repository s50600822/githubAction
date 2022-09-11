from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


ops = webdriver.FirefoxOptions()
ops.set_headless()
browser = webdriver.Firefox(firefox_options=ops)

browser.get('https://hoaphan.net')
print(browser.find_element(By.TAG_NAME, "body").text)

browser.quit()