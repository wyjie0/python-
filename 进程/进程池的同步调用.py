import os
import time
from multiprocessing import Pool

def func(n):
    print('start func%s'%n)
    time.sleep(1)
    print('end func%s'%n)

if __name__ == '__main__':
    p = Pool(5)
    for i in range(10):
        p.apply_async(func, args = (i,))
    p.close()
    p.join()#感知进程池中的任务执行结束