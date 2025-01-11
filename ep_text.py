#!/usr/bin/python

import ep_lib


def main():

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()

    ep_lib.set_font(3)
    ep_lib.text("test text draw",0,0,1)

    ep_lib.text("abcdefghijkl",0,20,0)

    ep_lib.set_font(1)
    ep_lib.text("abcdefghijklmnopq",0,45,0)
    ep_lib.text("abcdefghijklmnopqrstuv",0,60,0)
    ep_lib.text("abcdefghijklmnopqrstuvwxz",0,75,0)
    ep_lib.text("ABCDEFGHIJKLMNOPQRSTUVXYZ",0,90,1)
    
    ep_lib.set_font(2)
    ep_lib.text("!#$%&'()=~|{`}*+_?><",0,105,1)


if __name__ == '__main__':
    main()
