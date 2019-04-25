import time
import os


#多线程并发
# def func(a,b):
#     n = a + b
#     print(n,os.getpid())
# print('主：',os.getpid())
# for i in range(10):
#     t = Thread(target=func, args=(i,5))
#     t.start()

# class MyThread(Thread):
#     def __init__(self,arg):
#         super().__init__()
#         self.arg = arg
#
#     def run(self):
#         time.sleep(1)
#         print(self.arg)
#
# t = MyThread(10)
# t.start()
from threading import Thread
from multiprocessing import Process

def func(n):
    n-1

if __name__ == '__main__':
    t_lst = []
    start = time.time()
    for i in range(100):
        t = Thread(target=func,args=(i,))
        t.start()
        t_lst.append(t)
    for t in t_lst:t.join()
    t1 = time.time()-start
    t_lst = []
    start = time.time()
    for i in range(100):
        t = Process(target=func, args=(i,))
        t.start()
        t_lst.append(t)
    for t in t_lst: t.join()
    t2 = time.time() - start
    print(t1, t2)