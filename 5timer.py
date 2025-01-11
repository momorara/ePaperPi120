#!/usr/bin/python
"""
2025/01/11 新ライブラリに対応
"""
import ep_lib
import time

def hako_abs(x0,y0,d_width,heigth,color,n=0):
    x1 = d_width + x0
    y1 = heigth + y0
    ep_lib.rectangle(x0 , y0, x1, y1,"B",0)

def hako(x0,y0,d_width,heigth,n=0):
    # n番目の枠を塗る n=0,1,2,3,4
    xn = (x0 +2) + d_width *n + n *2
    yn = y0 +2
    for i in range(int(56/4)):
        width_n = d_width- i*4
        heigth_n = heigth -4 -i*4
        hako_abs(xn +i*2, yn +i*2, width_n, heigth_n,"B",0)
    hako_abs(xn +i*2+1, yn +i*2+1, 1, heigth_n-2,"B",0)

def main():

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()

    ep_lib.set_font(3)
    ep_lib.text("5minute timer",0,0,0)
    
    x0 = 0
    y0 = 25
    width =288 #外枠に1ドット空けて5つの内枠が入るようにする。
    # (width -4 -4)/5 = 288 内枠の幅は56となる)
    # 内側の枠は1ドット空けて描画する
    d_width= int((width -4 -4)/5)
    heigth = 102
    hako_abs(x0,y0,width,heigth,"B",0)

    # 枠を作る
    for i in range(5):
        x = (x0 +2) + d_width *i + i *2
        # print(x)
        hako_abs(x, y0 +2, d_width, heigth -4,"B",0)
    ep_lib.write_buffer()

    time.sleep(60)
    # n番目の枠を塗る n=0,1,2,3,4
    hako(x0,y0,d_width,heigth,n=0)
    ep_lib.write_buffer()
    time.sleep(60)
    hako(x0,y0,d_width,heigth,n=1)
    ep_lib.write_buffer()
    time.sleep(60)
    hako(x0,y0,d_width,heigth,n=2)
    ep_lib.write_buffer()
    time.sleep(60)
    hako(x0,y0,d_width,heigth,n=3)
    ep_lib.write_buffer()
    time.sleep(60)
    hako(x0,y0,d_width,heigth,n=4)

    ep_lib.text("up",130,0,1)
    

if __name__ == '__main__':
    main()
