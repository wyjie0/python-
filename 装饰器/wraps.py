import time
from functools import wraps

def wrapper(f):#f是被装饰的函数
    @wraps(f)
    def inner(*args, **kwargs):
        '''在被装饰函数之前要做的事'''
        ret = f(*args, **kwargs)#ret接收被装饰函数的返回值
        '''在被装饰函数之后要作恶事'''
        return ret
    return inner

#被装饰函数,可无参数，无返回值
@wrapper
def func(a, b):
    time.sleep(0.01)
    print('你好',a, b)
    return '大家好'

print(func.__name__)#获取函数的名字