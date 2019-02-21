#所有的客户端执行server端下发的指令
#将结果反馈回来，服务器接收

import subprocess

res = subprocess.Popen('dir',shell = True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE)
print(res.stdout.read().decode('gbk'))
print(res.stderr.read().decode('gbk'))