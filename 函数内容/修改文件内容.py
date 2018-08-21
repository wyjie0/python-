with open('wyjie', encoding='utf-8') as f, open('wyjie.bak', 'w', encoding='utf-8') as f2:
    for line in f:
        if '哈哈' in line:
            line = line.replace('哈哈', '阿娇')
        #写文件
        f2.write(line)

import os
os.remove('wyjie')
os.rename('wyjie.bak', 'wyjie')