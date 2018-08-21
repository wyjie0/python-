#装饰器形成的过程
#装饰器的作用
#原则：开放封闭原则
#装饰器的固定模式

#不想修改函数的调用方式，但是还想在原来的函数前后添加功能
#timmer就是一个装饰器函数，只是对一个函数有一些装饰作用
import time
#
# def timmer(f):#装饰器函数
#     def inner():
#         start = time.time()
#         ret = f()#被装饰函数
#         end = time.time()
#         print(end - start)
#         return ret
#     return inner
#
# @timmer         #语法糖  @装饰器函数名
# def func():     #被装饰函数
#     time.sleep(0.01)
#     print("大家好")
#     return '新年好'
# # func = timmer(func)
# ret = func()
# print(ret)


#原则：开放封闭原则
#开放：对扩展是开放的
#封闭：对修改是封闭的
#扩展：已有的函数不能修改，但是需要增加一些功能，那么就可以用装饰器，
#即：在函数外面增加一个函数来调用要改额函数，然后添加功能，最后在最外层
#再添加一个装饰函数

#装饰器的固定模式

#装饰函数
# def wrapper(f):#f是被装饰的函数
#     def inner(*args, **kwargs):
#         '''在被装饰函数之前要做的事'''
#         ret = f(*args, **kwargs)#ret接收被装饰函数的返回值
#         '''在被装饰函数之后要作恶事'''
#         return ret
#     return inner
#
# #被装饰函数,可无参数，无返回值
# @wrapper
# def func(a, b):
#     time.sleep(0.01)
#     print('你好',a, b)
#     return '大家好'

