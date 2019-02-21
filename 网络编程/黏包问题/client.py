import socket
import subprocess

sk = socket.socket()
sk.connect(('127.0.0.1', 8090))

cmd = sk.recv(1024).decode('gbk')
res = subprocess.Popen(cmd,shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
content = b'stdout:' + res.stdout.read()+b'stderr:'+res.stderr.read()
# sk.send(res.stdout.read())
# sk.send(res.stderr.read())
sk.send(content)

sk.close()