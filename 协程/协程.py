from greenlet import greenlet

def eat():
    print('eating start')
    g2.switch()
    print('eating end')

def play():
    print('playing start')
    g1.switch()
    print('playing end')

g1 = greenlet(eat)
g2 = greenlet(play)
g1.switch()
