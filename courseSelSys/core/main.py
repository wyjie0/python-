def login():
    '''
    登录函数，应该先到conf.config文件中读取userinfo的文件路径
    读取userinfo文件中的信息，对用户名和密码进行检查，
    登录成功之后，查看这个人的身份，来确定进入哪一个视图
    
    :return: 
    '''
    usr = input("请输入账号：")
    pwd = input("请输入密码：")

    pass

def main():
    '''
    打印欢迎信息
    调用login:得到返回值：用户的姓名和身份(三次登录)
    打印用户身份对应的功能菜单
    如果用户想要调用任何方法应该通过角色对象调用，跳转到对应对象的方法里
    
    :return: 
    '''
    print("欢迎进入选课系统！")
    login()