#reference: https://blog.csdn.net/hhs_1996/article/details/114186688 

from multiprocessing import Process, Queue, Lock
import time
global lock
lock=Lock()
 
def ProducerA(q1,q2):
    count = 1
    global lock
    while True:
        lock.acquire()
        q1.put(f"冷饮 {count}")
        print(f"{time.strftime('%H:%M:%S')} A 放入:[冷饮 {count}]")
        n=q2.get()
        print("q2 get, ",n)
        lock.release()
        count += 1
        time.sleep(1)
 
 
def ConsumerB(q1,q2):
    global lock
    while True:
        lock.acquire()
        print(f"{time.strftime('%H:%M:%S')} B 取出 [{q1.get()}]")
        q2.put("2")
        print("q2put")
        lock.release()
        time.sleep(2)
 
 
if __name__ == '__main__':
    q1 = Queue(maxsize=5)
    q2=Queue(maxsize=3)
    p = Process(target=ProducerA, args=(q1,q2))
    c = Process(target=ConsumerB, args=(q1,q2))
    c.start()
    p.start()
    c.join()
    p.join()