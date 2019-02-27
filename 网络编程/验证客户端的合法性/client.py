import socket
import hmac

secret_key = b'egg'
sk = socket.socket()
sk.connect(('127.0.0.1', 8080))


msg = sk.recv(32)
h = hmac.new(secret_key,msg)
digest = h.digest()
sk.send(digest)
sk.close()