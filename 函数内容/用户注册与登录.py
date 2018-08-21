

with open('wyjRegister', 'r+', encoding='utf-8') as f:
    zh = f.readline().strip()
    f.seek(0,1)
    k = f.readline().strip()
    i = 0
    while i < 3:
        account = input('请输入您的账号：')
        key = input('请输入您的密码')
        if zh != account:
            i += 1
            print('账号错误，请再输入一次，您还有{}次机会'.format(3-i))
            continue
        elif k != key:
            i += 1
            print('密码错误，请再输入一次，您还有{}次机会'.format(3 - i))
            continue
        else:
            print('登录成功')
            break
    if i == 3:
        print('再见')
'''

username = input('请输入您要注册的用户名:')
password = input('请输入你要注册的密码：')
with open('list_of_info','w',encoding='utf-8') as f:
    f.write('%s\n%s'%(username, password))
print('恭喜你注册成功')


li = []
i = 0
while i < 3:
    usn = input('请输入你的用户名：')
    pwd = input('请输入你的密码：')
    with open('list_of_info', 'r+', encoding='utf-8') as f1:
        for line in f1:
            li.append(line.strip('\n'))
    print(li)
    i += 1
'''
