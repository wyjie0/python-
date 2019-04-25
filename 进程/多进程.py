import os
import time
from multiprocessing import Process

def func():
    print(12345)
    time.sleep(1)
    print('子进程：',os.getpid())
    print('子进程的父进程:',os.getppid())
    print(54321)

if __name__ == '__main__':
    p = Process(target=func)#注册
    #p是一个进程对象
    p.start()
    print('*'*10)
    print('父进程：',os.getpid())
    print('祖宗进程：',os.getppid())