import time
from multiprocessing import Process

def func(arg1, arg2):
    print('*'*arg1)
    time.sleep(5)
    print('*'*arg2)

if __name__ == '__main__':
    p = Process(target=func, args=(10,20))
    p.start()
    p1 = Process(target=func, args=(10, 20))
    p1.start()
    p2 = Process(target=func, args=(10, 20))
    p2.start()