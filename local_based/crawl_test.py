from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from os import path

url="https://blog.csdn.net"
chrome_options =Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(executable_path='/Users/zhouromee/Desktop/ByteDance4/ByteDance_4th_Team19120623/local_based/chromedriver', chrome_options=chrome_options)
browser.get(url)
print("downloading link ", url)
page_text = browser.page_source
print(page_text)
browser.quit()
print("downloading done")