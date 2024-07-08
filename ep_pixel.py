#!/usr/bin/python

import ep_lib
import random

def main():

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()

    ep_lib.set_font(3)
    ep_lib.text("test randam 3000 pixels",0,0,1)

    for i in range(3000):
        x = random.randint(10, 290)
        y = random.randint(30, 125)
        ep_lib.pixel(x,y,"B",0)

    ep_lib.write_buffer()
    
    # ePaperをクローズ
    ep_lib.close()

if __name__ == '__main__':
    main()
