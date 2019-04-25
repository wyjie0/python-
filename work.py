# #用于正则表达式联系的数据生成器
# from random import randrange, choice, random
# from string import ascii_lowercase as lc
# from sys import maxsize
# import time,math
#
# tlds = ('com', 'edu', 'net', 'org', 'gov')
# with open('gendata.txt', 'w', encoding='utf-8') as f:
#
#     for i in range(randrange(5,11)):
#         dtint = math.floor(1e10 * random())
#         dtstr = time.ctime(dtint)
#         llen = randrange(4,8)
#         login = ''.join(choice(lc) for j in range(llen))
#         dlen = randrange(llen, 13)
#         dom = ''.join(choice(lc) for j in range(dlen))
#         content= '%s::%s@%s.%s::%d-%d-%d\n' %(dtstr,login,dom,choice(tlds),dtint,llen,dlen)
#         print(content)
#         # f.write(content)
#         f.writelines(content)

# import re
# data = "Thu Sep  5 19:34:11 2013::rixjd@cgwjaahpdt.gov::1378380851-5-10"
#
# patt = '-(\d)-'
# m = re.search(patt, data)
# print(m.group())

import re

pattern = r'(\d{4}-\d{6}-\d{5})|(\d{4}-\d{4}-\d{4}-\d{4})'
string1 = '2548-1234-1234-1234'
print(re.search(pattern,string1).group())
