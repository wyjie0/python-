#事件被创建的时候是False状态，导致wait()阻塞
#True状态的时候wait()不阻塞r

#用Event检测数据库是否可连接
import time,random
from threading import Thread,Event

def connect_db(e):
    count = 0
    while count <= 2:
        e.wait(1)
        if e.is_set() == True:
            print('连接数据库')
            break
        else:
            print('连接失败')
            count += 1
    else:
        raise TimeoutError('数据库连接超时')
def check_web(e):
    time.sleep(random.randint(0,4))
    e.set()

e = Event()
t1 = Thread(target=connect_db,args=(e,))
t2 = Thread(target=check_web,args=(e,))
t1.start()
t2.start()