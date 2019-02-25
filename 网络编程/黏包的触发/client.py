import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8090))

sk.send(b'hello')
sk.send(b'wyjie')

sk.close()