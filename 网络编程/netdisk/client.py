import socket
import os
import json
import struct

buffer = 4096

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
        elif res == 'Bye!':
            break
        else:
            print('IN UPLOADING.....')
            head = {'filepath':r'F:\python视频\Python全栈9期（第一部分）：基础+模块+面向对象+网络编程\day31',
                    'filename':r'03 python fullstack s9day33 黏包现象.mp4',
                    'filesize':None}
            file_path = os.path.join(head['filepath'],head['filename'])
            filesize = os.path.getsize(file_path)
            head['filesize'] = filesize
            json_head = json.dumps(head)    #字典转成了字符串
            bytes_head = json_head.encode('utf-8')       #字符串转成了bytes
            #计算head的长度
            head_size = len(bytes_head) #报头的大小
            print('head_size:',head_size)
            pack_size = struct.pack('i',head_size)

            sk.send(pack_size)#先发报头的大小
            sk.send(bytes_head)#再发报头
            with open(file_path,'rb') as f_obj:
                while filesize > 0:
                    # print(filesize)
                    if filesize >= buffer:
                        content = f_obj.read(buffer)
                        sk.send(content)
                        filesize -= buffer
                    else:
                        sk.send(f_obj.read(filesize))
                        filesize = 0
                        print('上传完毕')
                        break
            break
else: print(res)

sk.close()

# #发送端
#
# import socket
#
# sk = socket.socket()
# sk.connect(('127.0.0.1', 8090))