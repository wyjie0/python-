import time
from multiprocessing import Process

def func():
    while True:
        time.sleep(2)
        print('我还好')

if __name__ == '__main__':
    p = Process(target=func)
    p.daemon = True
    p.start()
    i = 0
    while i < 5:
        print('我是socket server')
        time.sleep(1)
        i+=1

#守护进程会随着主进程的代码完毕而执行完毕