from lxml import etree
from bs4 import BeautifulSoup
from multiprocessing import Process, Queue, Lock
from link_checker.link_checker import Link_checker

def get_new_url(key):
    global lock, pagetext_q, url_q
    page_text=text_by_key(key)
    tree=etree.HTML(page_text)
    #print("tree created")
    all_href=tree.xpath('//a')
    #print("all href: ",all_href)
    links=[]
        
    for href in all_href:
        links=href.xpath('./@href')
        if len(links)==0:
            continue
        link=links[0]
        #print("newlink: ",link)
        l_c=Link_checker(link)
        l_c_process=Process(target=l_c.add_link)
        l_c_process.start()
        l_c_process.join()

def get_content(key):
    '''
    get content from the pagetext leaded by the key,
    and store the content into database
    '''
    return