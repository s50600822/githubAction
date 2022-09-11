from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Firefox()

browser.get('https://youtu.be/AYG6JaoPBpY')

body = browser.find_element(By.TAG_NAME, "body")
#play it
body.send_keys(Keys.SPACE)

time.sleep(300)
browser.quit()