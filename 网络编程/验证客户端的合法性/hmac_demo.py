# #检测客户端是否合法，并不依靠登录认证
#
# import hmac
#
# h = hmac.new()
# cipher_text = h.digest()
import os
print(os.urandom(32))