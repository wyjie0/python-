import socket
from threading import Thread

def func(conn):
    conn.send(b'hhhh')
    msg = conn.recv(1024).decode('utf-8')
    print(msg)

    conn.close()

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
while True:
    conn, addr = sk.accept()
    t = Thread(target=func,args=(conn,))
    t.start()

sk.close()