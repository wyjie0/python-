import os
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,arg1,arg2):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2

    def run(self):
        print(os.getpid())
        print(self.name)
        print(self.arg1)
        print(self.arg2)

if __name__ == '__main__':
    print('主：',os.getpid())
    p1 = MyProcess('111','222')
    p1.start()
    p2 = MyProcess('333','444')
    p2.start()

#自定义类，继承Process类
#必须实现一个run方法，run方法中是在子进程中执行的代码