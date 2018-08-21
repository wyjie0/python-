# def generator():
#     print(123)
#     content = yield 1
#     print(content)
#     print(456)
#     yield 2
#
#
# g = generator()
# print(g.__next__())
# ret = g.send('hello')
# print('****',ret)

#send获取下一个值的效果和next基本一致
#只是在获取下一个值的时候，给上一个值的位置传递一个数据
    #使用send的注意事项
        #第一次使用生成器的时候，是用next获取下一个值
        #最后一个yield不能接受外部的值

#获取移动平均值
# def average():
#     sum = 0
#     count = 0
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num
#         count += 1
#         avg = sum / count
#
#
# avg_g = average()
# avg_g.__next__()
# ret = avg_g.send(10)
# ret = avg_g.send(40)
# print(ret)

def generator():
    a = 'abcde'
    b = '12345'
    yield from a#for i in a:yield i
    yield from b#for i in b: yield i

g = generator()
for i in g:
    print(i)