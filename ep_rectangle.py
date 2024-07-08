#!/usr/bin/python

import ep_lib
import random

def main():

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()

    ep_lib.set_font(3)
    ep_lib.text("test randam 30 rectangles",0,0,1)

    for i in range(30):
        x1 = random.randint(30, 290)
        y1 = random.randint(30, 120)
        x2 = random.randint(5, 30)
        y2 = random.randint(5, 30)
        if x1 + x2 > 290:
            x1 = x1 - x2
        if y1 + y2 > 125:
            y1 = y1 - y2
        ep_lib.rectangle(x1,y1,x2,y2,"B",0)

    ep_lib.write_buffer()
    
    # ePaperをクローズ
    ep_lib.close()

if __name__ == '__main__':
    main()
