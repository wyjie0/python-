# #动态参数有两种：可以接受任意个参数
#     #*args:接收的是按照位置传参的值，组织成一个元祖
#     #**kwargs:接收的是按照关键字传参的值，组织成一个字典
#     #*args必须在**kwargs之前
# #各种参数出现的位置：
#     #位置参数->*args->默认参数->**kwargs
# #如果默认参数的值是一个可变数据类型，
# #那么每一次调用函数的时候，如果不传值，就公用这个数据类型的资源
#
# #函数的嵌套定义：
# # def outer():
# #     def inner():
# #         print('inner')
# #
# # outer()#什么也不发生
#
# #nonlocal关键字：声明了一个上层的具有此声明变量的局部变量，且只能用于局部变量
#
# # a = 1
# # def outer():
# #     a = 1
# #     def inner():
# #         a = 2
# #         def inner2():
# #             nonlocal a
# #             a += 1
# #         inner2()
# #         print('##a## : ', a)
# #     inner()
# #     print('**a** : ', a)
# #
# # outer()
# # print('全局 : ', a)
#
# #函数名就是内存地址，且可以赋值
# # def func():
# #     print('你好')
#
# # func2 = func
# #
# # l = [func, func2]#函数名可以作为容器类型的元素
# # print(l)
# # for i in l:
# #     i()
#
# # def wahaha(f):
# #     f()
# #     return f
# #
# # qqxing = wahaha(func)#函数名可以作为函数的参数
# # qqxing()
#
# # def func(l):
# #     li = []
# #     i = 0
# #     for ele in l:
# #         if i % 2 == 1:
# #             li.append(ele)
# #         i += 1
# #     return li
# #
# # lis = [0,1,2,3,4,5,6]
# # print(func(lis))
#
# def count(s):
#     dig = 0
#     alpha = 0
#     spa = 0
#     other = 0
#     for i in s:
#         if i.isdigit():
#             dig += 1
#         elif i.isalpha():
#             alpha += 1
#         elif i.isspace():
#             spa += 1
#         else:
#             other += 1
#
#     return dig, alpha, spa, other
#
# d,a,s,o = count('asdf23  asdf;[')
# print(d,a,s,o)
#
# def func(filename, oldContent, newContent):
#     with open(filename, encoding='utf-8') as f,\
#         open('%s.bak'%filename, 'w', encoding='utf-8') as f2:
#         for line in f:
#             if oldContent in line:
#                 line = line.replace(oldContent, newContent)
#             f2.write(line)
#
#     import os
#     os.remove(filename)
#     os.rename('%s.bak'%filename, filename)
# def func(*args):
#     for i in args:
#         print(i)
#
# func(*(1,2,3,4))
