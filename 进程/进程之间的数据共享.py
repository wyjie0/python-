from multiprocessing import Manager,Process

def main(dic):
    pass

if __name__ == '__main__':
    m = Manager()
    dic = m.dict({'count':100})
    for i in range(50):
        p = Process(target=main,args=(dic,))
