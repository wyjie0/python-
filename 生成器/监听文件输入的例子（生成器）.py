def tail(filename):
    f = open(filename, encoding='utf-8')
    while True:
        line = f.readline()
        if line:
            yield line.strip()

g = tail('file')
for i in g:
    print(i)