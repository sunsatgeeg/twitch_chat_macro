from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

#os.system('chrome.bat')

#time.sleep(1)

#browser = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
#browser = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"C:\Users\Administrator\PycharmProjects\tellon join\chromedriver.exe" # Your Chrome Driver path
browser = webdriver.Chrome(chrome_driver, options=chrome_options)

browser.get("https://www.twitch.tv/popout/chu__s/chat?popout=")

try:
    elem = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'chat-input__textarea')))
except:
    print("실패")

time.sleep(1)

browser.find_element_by_tag_name('textarea').send_keys("GeeG")
#텔론_
try:
    elem = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'chu__s')))
except:
    print("실패")

print("Go")

browser.find_element_by_class_name('tw-align-items-center tw-core-button-label tw-flex tw-flex-grow-0').click()


