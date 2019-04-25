# import socket
#
# sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sk.connect(('127.0.0.1', 8080))
#
#
#
# while True:
#     data = input('>>>')
#     sk.send(data.encode('utf-8'))
#     rev = sk.recv(1024).decode('utf-8')
#     print(rev)
#
# sk.close()

import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input('>>>')

    if not data:
        break
    sk.sendto(data.encode('utf-8'), ('127.0.0.1', 8080))
    rev, addr = sk.recvfrom(1024)
    print(rev.decode('utf-8'))
sk.close()