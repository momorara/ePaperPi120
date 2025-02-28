#!/usr/bin/python

import ep_lib
import time
from PIL import Image

def main():

    print("画面を初期化して、白くする。")
    draw,image = ep_lib.image_set()
    ep_lib.clear_w(draw)

    # 既存の画像を開く 白黒画像に限る
    bitmap = Image.open("bmp/checker1.bmp")
    draw.bitmap((0, 0), bitmap, fill=None)
    # ep_lib.write_buffer()   
    ep_lib.ep_draw(0,0,image,0,1)
    time.sleep(1)
    ep_lib.clear_w(draw)


    bitmap = Image.open("bmp/checker2.bmp")
    draw.bitmap((0, 0), bitmap, fill=None)
    # ep_lib.write_buffer()   
    ep_lib.ep_draw(0,0,image,0,1)
    time.sleep(1)
    ep_lib.clear_w(draw)

    bitmap = Image.open("bmp/1bpp41.bmp")
    draw.bitmap((0, 0), bitmap, fill=None)
    # ep_lib.write_buffer()   
    ep_lib.ep_draw(0,0,image,0,1)
    time.sleep(1)
    ep_lib.clear_w(draw)

    bitmap = Image.open("bmp/Mountain_290x128wb.bmp")
    draw.bitmap((0, 0), bitmap, fill=None)
    # ep_lib.write_buffer()   
    ep_lib.ep_draw(0,0,image,0,1)
    # time.sleep(1)
    # ep_lib.clear_w(draw)

    
if __name__ == '__main__':
    main()


    # image_path = 'bmp/checker1.bmp'
    # image_path = 'bmp/checker2.bmp'
    # image_path = 'bmp/Mountain_250x128wb.bmp'
    # image_path = 'bmp/Mountain_200x100wb.bmp'
    # image_path = 'bmp/Mountain_290x128wb.bmp'
    # image_path = 'bmp/1bpp41.bmp'
