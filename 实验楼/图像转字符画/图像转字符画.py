import argparse
from PIL import Image

#命令行输入参数处理
arg = argparse.ArgumentParser()

arg.add_argument('file')#输入文件
arg.add_argument('-o','--output')#输出文件
arg.add_argument('--width',type = int,default=80)#输出字符画宽
arg.add_argument('--height', type = int, default=80)#输出字符画高

#获取参数
args = arg.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_chars = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#gray的值为0-256， 要映射到0-70之间必须让（gray/257）*70
def get_char(r, g, b, alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_chars)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_chars[int(gray/unit)]

if __name__ == '__main__':
    print(123)
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST )

    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)