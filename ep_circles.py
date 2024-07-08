#!/usr/bin/python

import ep_lib
import random

def main():

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()

    ep_lib.set_font(3)
    ep_lib.text("test randam 30 circles",0,0,1)

    for i in range(30):
        x1 = random.randint(30, 290)
        y1 = random.randint(30, 120)
        r = random.randint(3, 30)
        if x1 + r > 290:
            x1 = x1 - r
        if y1 + r > 125:
            y1 = y1 - r
        ep_lib.circle(x1,y1,r,"B",0)

    ep_lib.write_buffer()
    
    # ePaperをクローズ
    ep_lib.close()

if __name__ == '__main__':
    main()
