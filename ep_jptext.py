#!/usr/bin/python

import ep_lib
import time
from PIL import Image, ImageDraw, ImageFont

def main():

    print("画面を初期化して、白くする。")
    ep_lib.clear_w()

    # ビットマップ画像のサイズ
    image_width = 290
    image_height = 128

    # ゴシック
    font_path = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
    # 明朝体
    # font_path = '/usr/share/fonts/truetype/fonts-japanese-mincho.ttf'

    # フォントサイズ
    font_size = 20

    # 描画する日本語テキスト
    japanese_text = "こんにちは、世界！"

    # 新しい白黒画像を作成（モード1）
    image = Image.new("1", (image_width, image_height), 1)  # 1は白、0は黒

    # 描画用のオブジェクトを作成
    draw = ImageDraw.Draw(image)

    # フォントを読み込む
    font = ImageFont.truetype(font_path, font_size)

    # テキストを画像に描画
    text_position = (0, 0)  # テキストの位置（左上の座標）
    draw.text(text_position, japanese_text, font=font, fill=0)  # 0は黒
    font_size = 30
    font = ImageFont.truetype(font_path, font_size)
    text_position = (0, 20)  # テキストの位置（左上の座標）
    draw.text(text_position, japanese_text, font=font, fill=0)  # 0は黒
    font_size = 36
    font = ImageFont.truetype(font_path, font_size)
    text_position = (0, 50)  # テキストの位置（左上の座標）
    japanese_text = "日本語表示できた"
    draw.text(text_position, japanese_text, font=font, fill=0)  # 0は黒

    x,y = 0,0
    BorW = 0
    # 画像イメージをePaperに描画
    ep_lib.bmp_img(x,y,image,BorW,1)

    time.sleep(3)
    # 描画した内容をクリア
    draw.rectangle([0, 0, image.width, image.height], fill='white')

    japanese_text = "日本語表示できた"
    draw.text(text_position, japanese_text, font=font, fill=0)  # 0は黒
    ep_lib.bmp_img(x,y,image,BorW,1)

if __name__ == '__main__':
    main()
