#!/usr/bin/python
"""
2025/03/04  曜日を基本に表示
"""
import ep_lib
import datetime
import time
import numpy as np
from PIL import Image


def main():

    # 表示内容
    # 日付と曜日を表示
    # 14日火曜日
    # といった表示を行う

    draw, image = ep_lib.image_set()  # eペーパーディスプレイ用の描画オブジェクトと画像を取得
    ep_lib.clear_w(draw)  # 画面を白でクリア

    # 動作初回に表示
    wd_name = ["月","火","水","木","金","土","日"]
    now = datetime.datetime.now()
    wd_no = now.weekday()
    formatted_date = f"{int(now.day)}日"
    mes = formatted_date + wd_name[wd_no] + "曜日"
    draw.text((0, 30), mes, font=ep_lib.font_set("gos", 60), fill=0)
    ep_lib.ep_draw(0,0,image,0,1)
    
    last_date = datetime.datetime.now().date()   # 現在の日付を取得
    while True:

        time.sleep(60)  # 1分ごとにチェック
        current_date = datetime.datetime.now().date() 
        #日替わりのタイミングをチェック
        if current_date != last_date:
            print(f"日付が変わりました: {current_date}")
            last_date = current_date  # 日付を更新
            
            ep_lib.clear_w(draw)  # 画面を白でクリア

            # 表示文字を作って表示
            now = datetime.datetime.now()
            wd_no = now.weekday()
            formatted_date = f"{int(now.day)}日"
            mes = formatted_date + wd_name[wd_no] + "曜日"
            draw.text((0, 30), mes, font=ep_lib.font_set("gos", 60), fill=0)
            ep_lib.ep_draw(0,0,image,0,1)

            

if __name__ == "__main__":
    main()
