from multiprocessing import Pool

def func1(n):
    print('in func1')
    return n*n

def func2(nn):
    print('in func2')
    print(nn)

if __name__ == '__main__':
    p = Pool(5)
    p.apply_async(func1, args=(10,), callback=func2)
    p.close()
    p.join()