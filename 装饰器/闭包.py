#闭包：嵌套函数，内部函数调用外部函数的变量
# def outer():
#     a = 1
#     def inner():
#         print(a)
#     print(inner.__closure__)
# outer()

#使用闭包的常用方法
# def outer():
#     a = 1
#     def inner():
#         print(a)
#     return inner
#
# inn = outer()
# inn()

# import urllib
from  urllib.request import urlopen
# ret = urlopen('http://www.xiaohua100.cn/index.html').read()
# print(ret)
def get_url():
    url = 'http://www.xiaohua100.cn/index.html'
    def get():
        ret = urlopen(url).read()
        print(ret)
    return get

get_func = get_url()
get_func()