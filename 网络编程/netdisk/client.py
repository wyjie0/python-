import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
print("请输入账号和密码：")
acount = input("账号>>>")
passwd = input("密码>>>")
sk.send(bytes(acount,encoding='utf-8'))
sk.send(bytes(passwd,encoding='utf-8'))
res = sk.recv(1024).decode('utf-8')
if res == '登录成功！':
    print(res)
    res = sk.recv(1024).decode('utf-8')
    print(res)
    selection = input('>>>').encode('utf-8')
    sk.send(selection)
    print(type(selection))
    while True:
        res = sk.recv(1024).decode('utf-8')
        print(res)
        if res.startswith('ERROR'):
            selection = input('>>>').encode('utf-8')
            sk.send(selection)
        elif res == 'Bye!' or res.startswith('OK') :
            break
else: print(res)

sk.close()