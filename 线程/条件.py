from threading import Condition,Thread

def func(con, i):

    con.acquire()
    con.wait()
    print('in %sth function'%i)
    con.release()

con = Condition()
for i in range(10):
    Thread(target=func,args = (con,i)).start()
while True:
    num = int(input('>>>'))
    con.acquire()
    con.notify(num)
    con.release()