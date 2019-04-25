import time
import random
from multiprocessing import Process,JoinableQueue

def producer(name, food, q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        f = '%s生产了%s%s'%(name, food, i)
        print(f)
        q.put(f)
    q.join()        #阻塞 直到一个队列中的数据全部被取完

def consumer(q, name):
    while True:
        food = q.get()
        if food == None:
            print('%s获取了一个空'%name)
            break
        print('\033[31m%s消费了%s\033[0m' % (name, food))
        time.sleep(random.randint(1,3))
        q.task_done()

if __name__ == '__main__':
    q = JoinableQueue()
    p = Process(target=producer, args=('a','egg', q))
    p.start()
    p1 = Process(target=producer, args=('b','app', q))
    p1.start()
    c = Process(target=consumer, args=(q, 'cc'))
    c.start()
    c2 = Process(target=consumer, args = (q, 'dd'))
    c2.start()
    c.daemon = True
    c2.daemon = True
    p.join()
    p1.join()

#在消费者这一端：
    #每次获取一个数据
    #处理一个数据
    #发送一个记号，标志一个数据被处理成功

#在生产者这一端：
    #每一次生产一个数据
    #且每一次生产的数据都放在队列中
    #在队列中刻上一个记号
    #当生产者全部生产完毕后发送一个join信号，表示停止生产数据，且要等待之前被刻上的记号都被消费完
    #当数据都被处理完时，join结束