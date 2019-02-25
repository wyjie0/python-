import socket
import subprocess
import struct

sk = socket.socket()
sk.connect(('127.0.0.1', 8090))

while True:
    cmd = sk.recv(1024).decode('gbk')
    if cmd == 'q':
        break
    res = subprocess.Popen(cmd, shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    std_out = res.stdout.read()
    std_err = res.stderr.read()
    size = struct.pack('i',len(std_out)+len(std_err))
    sk.send(size)
    sk.send(std_out)
    sk.send(std_err)