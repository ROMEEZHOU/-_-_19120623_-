from multiprocessing import Pool
from multiprocessing import Process, Queue, Lock
import crawler.crawler
from manager.AbstractManager import AbstractManager
import time

class Crawler_manager(AbstractManager):
    def __init__(self,process_n):
        self.process_n=process_n
        global lock, url_q, pagetext_q

    def run(self):
        global lock, url_q, pagetext_q
        url_list=[]
        while True:
            if url_q:
                url_list.append(url_q.get())
                if len(url_list)==process_n:
                    pool=Pool(processes=self.process_n)
                    pool.map(crawler.crawler.run_crawler,url_list)
                    '''
                    crawler_multi=Crawler_multi(self.process_n, url_list)
                    crawler_process=Process(target=crawler_multi.start_process,args=(self.process_n,url_list))
                    crawler_process.start()
                    crawler_process,join()
                    '''
                    url_list=[]
            time.sleep(2)

    def stop(self):
        pass

    def check_alive(self):
        pass

    def detect_failure(self):
        pass

    def roll_back(self):
        pass