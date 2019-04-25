import time
import random
from multiprocessing import Process
from multiprocessing import Semaphore

def ktv(i, sema):
    sema.acquire()#获取钥匙
    print('%s走进ktv'%i)
    time.sleep(random.randint(1,5))
    print('%s走出ktv'%i)
    sema.release()
if __name__ == '__main__':
    sema = Semaphore(4)
    for i in range(20):
        p = Process(target=ktv, args=(i,sema))
        p.start()