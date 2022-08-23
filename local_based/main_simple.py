from multiprocessing import Process, Queue, Lock
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
from bs4 import BeautifulSoup
import os
from os import path

global lock
lock=Lock()

def crawl(url_q, page_q):
    global lock
    while True:
        lock.acquire()
        url=url_q.get()
        print("got link ", url)
        lock.release()
        print("now download")
        try:
            chrome_options =Options()
            chrome_options.add_argument('--headless')
            browser = webdriver.Chrome(executable_path='/Users/zhouromee/Desktop/ByteDance4/ByteDance_4th_Team19120623/local_based/chromedriver', chrome_options=chrome_options)
            browser.get(url)
            print("downloading link ", url)
            page_text = browser.page_source
            #print(page_text)
            browser.quit()
            print("downloading done")
        except Exception as e:
            continue
        lock.acquire()
        print("put page")
        page_q.put(page_text)
        print("put page done, ", page_q)
        lock.release()
        time.sleep(2)

'''
def get_by_selenium(url):
    try:
        chrome_options =Options()
        chrome_options.add_argument('--headless')
        option=ChromeOptions()
        browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options, option=option)
        browser.get(url)
        print("downloading link ", url)
        page_text = browser.page_source
        browser.quit()
        print("downloading done")
        return page_text
    except Exception as e:
        return ''
'''

def get_new_url(url_q,page_q):
    global lock
    while True:
        lock.acquire()
        page_text=page_q.get()
        print("got page")
        lock.release()
        try:
            tree=etree.HTML(page_text)
            print("tree created")
            all_href=tree.xpath('//a')
            print("all href: ",all_href)
            links=[]
        
            for href in all_href:
                links=href.xpath('./@href')
                if len(link)==0:
                    continue
                link=link[0]
                lock.acquire()
                print("newlink: ",link)
                url_q.put(link)
                lock.release()
                time.sleep(1)
        except:
            continue
            

if __name__=="__main__":
    url_q=Queue(maxsize=10)
    page_q=Queue(maxsize=10)
    url_q.put("https://blog.csdn.net")
    crawl_url=Process(target=crawl, args=(url_q,page_q))
    new_url=Process(target=get_new_url, args=(url_q, page_q))
    crawl_url.start()
    new_url.start()
    crawl_url.join()
    new_url.join()