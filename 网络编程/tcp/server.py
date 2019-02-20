import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()

conn,addr = sk.accept()
while True:
    ret = conn.recv(1024).decode('utf-8')
    print(ret)
    message = input(">>>")
    conn.send(bytes(message,encoding='utf-8'))