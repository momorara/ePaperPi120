#!/usr/bin/python

import ep_lib
import random

def main():

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()

    ep_lib.set_font(3)
    ep_lib.text("test randam 30 lines",0,0,0)
    ep_lib.rectangle(0,30,292,127,"B",1)
    for i in range(80):
        x1 = random.randint(0, 292)
        y1 = random.randint(30, 127)
        x2 = random.randint(0, 292)
        y2 = random.randint(30, 127)
        ep_lib.line(x1,y1,x2,y2,"B",0)
    ep_lib.write_buffer()
    
    # ePaperをクローズ
    ep_lib.close()

if __name__ == '__main__':
    main()
