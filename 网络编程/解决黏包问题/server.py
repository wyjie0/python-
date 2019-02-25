import socket
import struct

sk = socket.socket()
sk.bind(('127.0.0.1', 8090))
sk.listen()

conn, addr = sk.accept()
while True:
    cmd = input('>>>').encode('gbk')
    if cmd == 'q':
        conn.send(b'bye')
        break
    conn.send(bytes(cmd))
    size = conn.recv(4)
    size = struct.unpack('i',size)[0]
    print(size)
    ret = conn.recv(int(size)).decode('gbk')
    print(ret)
    # ret = conn.recv(int(size)).decode('utf-8')
    # print(ret)

conn.close()
sk.close()