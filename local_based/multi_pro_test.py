#reference: https://blog.csdn.net/Hao_ge_666/article/details/120571731

import multiprocessing
import time

#buffer=Queue(10)
#empty=Semaphore(2)
#full=Semaphore(0)
lock=multiprocessing.Lock()

def eat(num):
    for i in range(num):
        lock.acquire()
        print("eat")
        lock.release()
        time.sleep(1)

def drink(num):
    for i in range(num):
        lock.acquire()
        print(drink)
        lock.release()
        time.sleep(1)

if __name__=='__main__':
    eat_process=multiprocessing.Process(target=eat,args=(3,))
    drink_process=multiprocessing.Process(target=drink,args=(4,))

    eat_process.start()
    drink_process.start()