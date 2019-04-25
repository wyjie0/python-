#通过一个信号 来控制多个进程同时 执行或阻塞
# from multiprocessing import Event
# # 一个信号可以使所有的进程都进入阻塞状态，也可以控制所有的进程解除阻塞
# # 一个事件被创建之后，默认是阻塞状态
# e = Event()#创建了一个事件
# print(e.is_set())   #查看一个事件的状态，默认为阻塞
# e.set()#将这个事件的状态设置为True
# e.wait()#根据e.is_set()的值来决定是否在wait处阻塞

# 红绿灯事件
import time
import random
from multiprocessing import Event,Process

def car(e, i):
    if not e.is_set():
        print('car%i在等待'%i)
        e.wait()#阻塞，直到得到一个事件状态改变，变成True的xinhao
    print('\033[0;32;40mcar%i通过\033[0m' % i)


def traffic_light(e):
    while True:
        if e.is_set():
            e.clear()
            print('\033[31m红灯亮了\033[0m')
        else:
            e.set()
            print('\033[32m红灯亮了\033[0m')
        time.sleep(2)
if __name__ == '__main__':
    e = Event()
    p = Process(target=traffic_light,args=(e,))
    p.start()
    for i in range(20):
        cars = Process(target=car, args=(e,i))
        cars.start()
        time.sleep(random.random())