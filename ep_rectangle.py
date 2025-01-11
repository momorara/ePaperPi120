#!/usr/bin/python

import ep_lib
import random

def main():

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()

    ep_lib.set_font(3)
    ep_lib.text("test randam 30 rectangles",0,0,0)
    ep_lib.rectangle(0,30,292,127,"B",1)
    for i in range(30):
        x1 = random.randint(0, 260)
        y1 = random.randint(30, 120)
        x2 = x1 + random.randint(5, 30)
        y2 = y1 + random.randint(5, 30)
        if x2 > 290:
            x1 = 290
        if y2  > 127:
            y2 = 127
        ep_lib.rectangle(x1,y1,x2,y2,"B",0)

    ep_lib.write_buffer()
    

if __name__ == '__main__':
    main()
