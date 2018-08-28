#作用域相关内置函数
#locals()和globals()
# print(locals())#返回本地作用域中的所有名字
# print(globals())#返回全局作用域中的所有名字

#迭代器.__next()  <-->   next(迭代器)
#迭代器 = iter(可迭代的)   <-->   迭代器 = 可迭代的.__iter__()

#dir()查看一个变量拥有的方法

#callable(),判断是否能够被调用
# print(callable(print))#True
# print(callable(2))#False

# help()
# help(str)

#字符串形式代码的执行
# exec ('print(123)')
# eval('print(123)')
# print(eval('1+2+3'))#有返回值
# print(exec('1+2+3'))#无返回值
#exec和eval都可以执行字符串类型的代码
#eval有返回值，适合处理有结果的简单计算
# exec没有返回值， 适合处理简单的流程控制
#eval只能用在你们明确知道你要执行的代码是什么

d = {'a' : 1, 'b' : 2, 'c' : 3}
for item ,v in d.items():
    print(item)
    print(v)
