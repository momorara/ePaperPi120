#!/usr/bin/python

import ep_lib
import random

def main():

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()

    ep_lib.set_font(3)
    ep_lib.text("test randam 30 circles",0,0,0)
    ep_lib.rectangle(0,30,292,127,"B",1)

    for i in range(30):
        x1 = random.randint(30, 260)
        y1 = random.randint(60, 97)
        r = random.randint(3, 30)
        ep_lib.circle(x1,y1,r,"B",0)

    ep_lib.write_buffer()
    

if __name__ == '__main__':
    main()
