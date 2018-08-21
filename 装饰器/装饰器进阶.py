## 带参数的装饰器
#可以控制所有带装饰器的函数是否使用该装饰器
# import time
#
# # FLAG = True
# FLAG = False
# def timmer_out(flag):
#     def timmer(func):
#         def inner(*args, **kwargs):
#             if flag:
#                 start = time.time()
#                 ret = func(*args, **kwargs)
#                 end = time.time()
#                 print(end - start)
#                 return ret
#             else:
#                 ret = func(*args, **kwargs)
#                 return ret
#
#         return inner
#     return timmer
#
#
# @timmer_out(FLAG)
# def wahaha():
#     time.sleep(0.1)
#     print('wahahaha')
#
# @timmer_out(FLAG)
# def erguotou():
#     time.sleep(0.1)
#     print('erguotou')
#
# wahaha()
# erguotou()

##多个装饰器装饰一个函数
def wrapper1(func):#func --> f
    def inner1():
        print('1,before')
        func()  #func --> f
        print('1,after')
    return inner1

def wrapper2(func):#func --> inner1
    def inner2():
        print('2,before')
        func()  #func-->inner1
        print('2, after')
    return inner2

@wrapper2#f = wrapper2(f) --> wrapper2(inner1) == inner2
@wrapper1#f = wrapper1(f) = inner1
def f():    #f --> inner2
    print('in f')

f()


