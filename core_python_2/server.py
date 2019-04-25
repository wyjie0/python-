# import time
# import socket
# sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# sk.bind(('127.0.0.1', 8080))
# sk.listen()
#
# while True:
#     conn,addr = sk.accept()
#     while True:
#         ret = conn.recv(1024).decode('utf-8')
#         date = time.ctime(time.time())
#         message = '['+date+']'+ret
#         conn.send(message.encode('utf-8'))
#     conn.close()
#
# sk.close()

import socket
import time

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sk.bind(('127.0.0.1', 8080))

while True:
    rev, addr = sk.recvfrom(1024)
    if not rev:
        break
    message = '[%s] %s'%(time.ctime(),rev.decode('utf-8'))
    sk.sendto(message.encode('utf-8'), addr)

sk.close()