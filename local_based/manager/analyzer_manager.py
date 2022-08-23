from multiprocessing import Pool
from multiprocessing import Process, Queue, Lock
import analyzer.analyzer
from manager.AbstractManager import AbstractManager
import time

class Analyzer_manager(AbstractManager):
    def __init__(self):
        global lock, url_q, pagetext_q

    def run(self):
        global lock, url_q, pagetext_q
        while True:
            if pagetext_q:
                url=pagetext_q.get()
                analyzer_process=Process(target=analyzer.analyzer.get_new_url,args=(url,))
                analyzer_process.start()
                analyzer_process.join()
            time.sleep(2)

    def stop(self):
        pass

    def check_alive(self):
        pass

    def detect_failure(self):
        pass

    def roll_back(self):
        pass