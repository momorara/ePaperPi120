#!/usr/bin/python

import ep_lib
import random

def main():

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()

    ep_lib.set_font(3)
    ep_lib.text("test randam 3000 pixels",0,0,0)
    ep_lib.rectangle(0,30,292,127,"B",1)
    for i in range(3000):
        x = random.randint(0, 292)
        y = random.randint(30, 127)
        ep_lib.pixel(x,y,"B",0)
    ep_lib.write_buffer()
    
    # ePaperをクローズ
    ep_lib.close()

if __name__ == '__main__':
    main()
