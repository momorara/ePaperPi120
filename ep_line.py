#!/usr/bin/python

import ep_lib
import random

def main():

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()

    ep_lib.set_font(3)
    ep_lib.text("test randam 30 lines",0,0,1)

    for i in range(80):
        x1 = random.randint(10, 290)
        y1 = random.randint(30, 125)
        x2 = random.randint(10, 290)
        y2 = random.randint(30, 125)
        ep_lib.line(x1,y1,x2,y2,"B",0)

    ep_lib.write_buffer()
    
    # ePaperをクローズ
    ep_lib.close()

if __name__ == '__main__':
    main()
