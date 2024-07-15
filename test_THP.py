#!/usr/bin/python
"""
2024/07/14  日時と気温、湿度、気圧の表示を行う

"""
import ep_lib
from PIL import Image, ImageDraw, ImageFont

import datetime
import time

def main():

    path = '/home/pi/ePaperPi/'  # cronで起動するには絶対パスが必要

    # 表示内容
    # 2024年11月14日(日)
    # 11時24分
    # 24度 50% 1012hPa
    # といった表示を行う


    # ビットマップ画像のサイズ
    image_width = 290
    image_height = 128

    # ゴシック
    font_path = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
    # 明朝体
    # font_path = '/usr/share/fonts/truetype/fonts-japanese-mincho.ttf'

    # 新しい白黒画像を作成（モード1）
    image = Image.new("1", (image_width, image_height), 1)  # 1は白、0は黒

    # 描画用のオブジェクトを作成
    draw = ImageDraw.Draw(image)

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()
    # ep_lib.clear_b()
    # ep_lib.clear_w()


    while True:

        # 2024年11月14日(日)
        now = datetime.datetime.now()
        wd_no = now.weekday()
        # print(wd_no)
        wd_name = ["月","火","水","木","金","土","日"]
        # print(wd_name[wd_no])

        # AHT,BMPの有無を確認して表示内容を変える
        # ない場合は、時計のみとする

        # フォントサイズ
        font_size = 30
        # フォントを読み込む
        font = ImageFont.truetype(font_path, font_size)

        mes = now.strftime("%Y年%m月%d日") + "(" + wd_name[wd_no] + ")"
        print(mes)
        # テキストを画像に描画
        text_position = (0, 0)  # テキストの位置（左上の座標）
        draw.text(text_position, mes, font=font, fill=0)  # 0は黒

        # 11時24分
        mes = now.strftime(" %H時%M分 ")
        # フォントサイズ
        font_size = 36
        # フォントを読み込む
        font = ImageFont.truetype(font_path, font_size)
        print(mes)
        # テキストを画像に描画
        text_position = (50, 40)  # テキストの位置（左上の座標）
        draw.text(text_position, mes, font=font, fill=0)  # 0は黒

        # 気温、湿度、気圧を読み取り
        with open(path + 'temp_data_last.txt') as f:
            temp = f.read()
            temp = str(int(temp) /10)
        with open(path + 'humdy_data_last.txt') as f:
            humdy = f.read()
        with open(path + 'press_data_last.txt') as f:
            press = f.read()
        # print(temp,humdy,press)
        mes = "" + temp + "度 " + humdy + "% " + press + "hPa"
            # フォントサイズ
        font_size = 28
        # フォントを読み込む
        font = ImageFont.truetype(font_path, font_size)
        print(mes)
        # テキストを画像に描画
        text_position = (0, 90)  # テキストの位置（左上の座標）
        draw.text(text_position, mes, font=font, fill=0)  # 0は黒

        x,y = 0,0
        BorW = 0
        # 画像イメージをePaperに描画
        ep_lib.bmp_img(x,y,image,BorW,1)

        # 描画用のオブジェクトをクリアする（白で塗りつぶす）
        draw.rectangle([0, 0, image_width, image_height], fill=1)

        # 正分になるのを待つ
        dt_now = datetime.datetime.now()
        while dt_now.second != 0:
            # print(dt_now.second)
            dt_now = datetime.datetime.now()
            time.sleep(0.01)
        # print('{0:.2f}'.format(time.time() ))

if __name__ == "__main__":
    main()
