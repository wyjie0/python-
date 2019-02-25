import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8090))
sk.listen()

conn, addr = sk.accept()

ret1 = conn.recv(12)
ret2 = conn.recv(10)

print(ret1)
print(ret2)

conn.close()
sk.close()