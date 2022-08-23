from multiprocessing import Process, Queue, Lock
from manager.AbstractManager import AbstractManager
from manager.analyzer_manager import Analyzer_manager
from maneger.crawler_manager import Crawler_manager
import time

class All_manager(AbstractManager):
    def __init__(self,root_url,q1,q2,process_n):
        global lock, url_q, pagetext_q
        self.root_url=root_url
        self.q1=q1
        self.q2=q2
        self.process_n=process_n

    def run(self):
        global lock, url_q, pagetext_q
        url_q=Queue(maxsize=self.q1)
        pagetext_q=Queue(maxsize=self.q2)
        url_q.put(self.root_url)
        lock=Lock()
        crawl=Crawler_manager(process_n)
        analyze=Analyzer_manager()
        crawl_p=Process(target=crawl.run)
        analyze_p=Process(target=analyze.run)
        crawl_p.start()
        analyze_p.start()
        crawl_p.join()
        analyze_p.join()

    def stop(self):
        pass

    def check_alive(self):
        pass

    def detect_failure(self):
        pass

    def roll_back(self):
        pass