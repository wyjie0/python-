import socketserver

#socketserver起的客户端可以同时和多个客户端通信

#必须继承socketserver.BaseRequestHandler
#必须实现handle函数
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            ret = self.request.recv(1024).decode('utf-8')
            if ret == 'q':
                self.request.close()
                break
            else:
                print(ret)
                msg = input('>>>').encode('utf-8')
                self.request.send(msg)
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyServer)

    server.serve_forever()