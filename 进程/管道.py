#实现生产者消费者模型
import time
import random
from multiprocessing import Pipe, Process

def producer(con, pro, name, food):
    con.close()
    for i in range(10):
        time.sleep(random.random())
        f = '%s生产%s%s'%(name, food, i)
        print(f)
        pro.send(f)
    pro.close()

def consumer(con, pro, name):
    pro.close()
    while True:
        try:
            food = con.recv()
            print('%s吃了%s'%(name, food))
            time.sleep(random.randint(2,3))
        except EOFError:
            con.close()
            break

if __name__ == '__main__':
    con, pro = Pipe()
    p = Process(target=producer,args=(con, pro, 'aaa', '糖'))
    p.start()
    c = Process(target=consumer,args=(con, pro, 'bbb'))
    c.start()
    c1 = Process(target=consumer,args=(con, pro, 'ccc'))
    c1.start()
    con.close()
    pro.close()