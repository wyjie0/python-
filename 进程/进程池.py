import time
from multiprocessing import Pool,Process

def func(n):
    for i in range(10):
        n += 1

if __name__ == '__main__':
    start = time.time()
    pool = Pool(5)
    pool.map(func, range(100))

    t1 = time.time()-start

    start = time.time()
    p_list = []
    for i in range(100):
        p = Process(target = func, args=(i,))
        p_list.append(p)
        p.start()
    for i in p_list:
        i.join()
    t2 = time.time()-start
    print(t1, t2)