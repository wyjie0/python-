import socket
import subprocess

sk = socket.socket()
sk.bind(('127.0.0.1', 8090))
sk.listen()

conn,addr = sk.accept()
conn.send(b'dir;ls')
res= conn.recv(1024).decode('gbk')
print(res)
# print(err)

conn.close()
sk.close()

#TCP会黏包，但是不会丢包