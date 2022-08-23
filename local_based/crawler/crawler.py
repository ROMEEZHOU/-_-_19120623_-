from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from os import path
from multiprocessing import Process, Queue, Lock


webdriver='/Users/zhouromee/Desktop/ByteDance4/ByteDance_4th_Team19120623/local_based/chromedriver'

def get_pagetext(url):
    '''url: string of url'''
    global lock
    chrome_options =Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(executable_path=self.webdriver, chrome_options=chrome_options)
    browser.get(url)
    #print("downloading link ", url)
    page_text = browser.page_source
    #print(page_text)
    browser.quit()
    #print("downloading done")
    return page_text

def put_pagetext(url):
    global lock, pagetext_q
    lock.acquire()
    pagetext_q.put(pagetext)
    lock.release()

def store(url,page_text):
    global lock
    pass

def run_crawler(url):
    global lock, pagetext_q
    pagetext=get_pagetext(url)
    put_pagetext(url)
    #store(url,pagetext)
