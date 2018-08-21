#列表推导式
# egg_list = ['鸡蛋%s'%i for i in range(10)]
# print(egg_list)
#
# print([i*i for i in range(10)])
# #生成器表达式
# g = (i for i in range(10))
# print(g)
# for i in g:
#     print(i)

#列表推导式和生成器表达式的区别
    #括号不一样
    #返回的值不一样====生成器表达式几乎不占用内存

g = (i*i for i in range(10))
