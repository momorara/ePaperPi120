#!/usr/bin/python

import ep_lib
# import random

def main():

    print("画面を初期化して、白くしテスト用の四角を書く")
    draw,image = ep_lib.image_set()
    ep_lib.clear_w(draw)

    de = 0
    dd = 2

    draw.rectangle((0, 0, 291, 119 ), outline="black", fill="white")
    draw.rectangle((0+dd, 0+dd +de, 291-dd, 119-dd +de), outline="black", fill="white")
    dd += 2
    draw.rectangle((0+dd, 0+dd +de, 291-dd, 119-dd +de), outline="black", fill="white")
    dd += 2
    draw.rectangle((0+dd, 0+dd +de, 291-dd, 119-dd +de), outline="black", fill="white")
    dd += 2
    draw.rectangle((0+dd, 0+dd +de, 291-dd, 119-dd +de), outline="black", fill="white")

    draw.text((45, 0 +de),"test", font=ep_lib.font_set("gos",100) ,fill=0)

    ep_lib.ep_draw(0,0,image,0,1)
    # SPI を終了（リソースを解放）
    ep_lib.close()

if __name__ == '__main__':
    main()
