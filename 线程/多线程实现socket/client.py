import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

msg = sk.recv(1024)
print(msg)
inp = input('>>>').encode('utf-8')

sk.send(inp)

sk.close()