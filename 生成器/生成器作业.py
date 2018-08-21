#处理文件，用户指定要查找的文件和内容，将文件中包含要查找内容的每一行都输出到屏幕
def findContent(content):
    with open('装饰器.py', encoding='utf-8') as f:
        for i in f:
            if content in i:
                yield i

g = findContent('装饰器啊')
for i in g:
    print(i.strip())