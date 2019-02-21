import socket

func = ['上传','下载']
flag = False
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn,addr = sk.accept()

user_acount = conn.recv(1024).decode('utf-8')
user_passwd = conn.recv(1024).decode('utf-8')
with open('userinfo') as f:
    for line in f:
        acount,passwd = line.strip().split('|')
        if acount == user_acount and passwd == user_passwd:
            conn.send(bytes('登录成功！', encoding='utf-8'))
            flag = True
            # conn.send(bytes('登录成功！\n输入编号选择功能:',encoding='utf-8'))
            # conn.send(bytes('1:%s\n2:%s'%(func[0],func[1]),encoding='utf-8'))
        else:
            conn.send(bytes('登录失败！', encoding='utf-8'))
    if flag:
        conn.send(bytes('输入编号选择功能:\n1:%s\n2:%s'%(func[0],func[1]), encoding='utf-8'))
        # conn.send(bytes('1:%s\n2:%s'%(func[0],func[1]),encoding='utf-8'))
        res = conn.recv(1024).decode('utf-8')
        while True:
            print(type(res))
            if res == 'q':
                conn.send(b'Bye!')
                break
            elif res == '1' or res == '2':
                conn.send(b'OK!Wait....')
                break
            else:
                conn.send(bytes('ERROR:请输入正确的编号！', encoding='utf-8'))
                res = conn.recv(1024).decode('utf-8')

conn.close()
sk.close()