#只要含有yield关键字的函数都是生成器函数，且yield不能和return共用
# def generator():
#     print(1)
#     yield 'a'
# #生成器函数：执行之后会得到一个生成器作为返回值
# ret = generator()
# print(ret)

# def generator():
#     print(1)
#     yield 'a'
#     print(2)
#     yield 'b'
#     print(3)
#yield能返回值，但是不会终止一个函数
# g = generator()
# ret = g.__next__()
# print(ret)
# ret = g.__next__()
# print(ret)
# ret = g.__next__()
# print(ret)
# for i in g:
#     print(i)

def wahaha():
    for i in range(2000000):
        yield '娃哈哈%s'%i

g = wahaha()#g是一个生成器
for i in g:
    print(i)