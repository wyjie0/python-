from multiprocessing import Queue,Process

def produce(q):
    q.put('hello')

def consume(q):
    print(q.get())

if __name__ == '__main__':
    q = Queue()
    p = Process(target=produce, args=(q,))
    p.start()
    c = Process(target=consume, args=(q,))
    c.start()
