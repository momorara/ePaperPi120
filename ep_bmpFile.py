#!/usr/bin/python

import ep_lib
import time

def main():

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()

    ep_lib.set_font(3)
    ep_lib.text("test bmpFile",30,30,1)

    x,y = 20,0
    BorW = 1

    image_path = 'bmp/checker1.bmp'
    ep_lib.bmp(x,y,image_path,BorW,1)
    time.sleep(2)
    # ep_lib.clear_w()

    image_path = 'bmp/zero_250x128.bmp'
    ep_lib.bmp(x,y,image_path,BorW,1)
    time.sleep(2)
    ep_lib.clear_buffer()

    image_path = 'bmp/1bpp41.bmp'
    ep_lib.bmp(x,y,image_path,BorW,1)
    time.sleep(2)
    # ep_lib.clear_w()

    image_path = 'bmp/Mountain_250x128wb.bmp'
    BorW = 0
    ep_lib.bmp(x,y,image_path,BorW,1)
    time.sleep(2)
    BorW = 1
    ep_lib.bmp(x,y,image_path,BorW,1)
    time.sleep(3)
    # ep_lib.clear_w()
    
if __name__ == '__main__':
    main()


    # image_path = 'bmp/checker1.bmp'
    # image_path = 'bmp/checker2.bmp'
    # image_path = 'bmp/Mountain_250x128wb.bmp'
    # image_path = 'bmp/Mountain_200x100wb.bmp'
    # image_path = 'bmp/Mountain_290x128wb.bmp'
    # image_path = 'bmp/zero_250x128.bmp'
    # image_path = 'bmp/1bpp41.bmp'
