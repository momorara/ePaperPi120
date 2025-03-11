#!/usr/bin/python
"""
2024/07/14  日時と気温、湿度、気圧の表示を行う
2024/07/15  気圧を60回記録して、上昇か下降かを判別して表示
2024/07/16  気圧を関数化と修正
2025/01/11  新ライブラリに対応
2025/01/18  再度改造した新ライブラリに対応
2025/02/25  計測値あり、なしで表示を変える
"""
import ep_lib
import datetime
import time
import numpy as np
from PIL import Image



def press_higt_low(pressure_data):
    # 移動平均を計算する（例として5分間隔の移動平均）
    window_size = 5
    moving_avg = np.convolve(pressure_data, np.ones(window_size)/window_size, mode='valid')
    # 直近の30分間のデータを使用する
    X = np.arange(30)
    y = moving_avg[-30:]
    # 平均値を引いて中心化
    X_centered = X - X.mean()
    y_centered = y - y.mean()
    # 傾きを計算
    slope = np.sum(X_centered * y_centered) / np.sum(X_centered**2)
    # 判定基準（傾きが0に近い場合は「変わらない」とする）
    threshold = 0.01  # データに応じて調整可能
    # 傾向を判定
    if slope > threshold:
        result = "気圧は上がっています"
        high_or_low = 1
    elif slope < -threshold:
        result = "気圧は下がっています"
        high_or_low = 2
    else:
        result = "気圧は変わりません"
        high_or_low = 3
    # print(result,high_or_low)
    # print(pressure_data)
    return high_or_low

def main():

    # 計測値あり、なしで表示を変える
    THP=1 # 計測値あり
    THP=0 # 計測値なし

    path = '/home/pi/ePaperPi/'  # cronで起動するには絶対パスが必要

    # 表示内容
    # 2024年11月14日(日)
    # 11時24分
    # 24度 50% 1012hPa
    # といった表示を行う

    draw, image = ep_lib.image_set()  # eペーパーディスプレイ用の描画オブジェクトと画像を取得
    ep_lib.clear_w(draw)  # 画面を白でクリア

    press_34 = []
    # press_34 = [
    # 1011, 1019, 1013, 1013, 1013, 1013, 1013, 1013, 1014, 1013,
    # 1013, 1015, 1014, 1015, 1014, 1013, 1013, 1013, 1014, 1013,
    # 1015, 1013, 1013, 1015, 1014, 1014, 1015, 1014, 1014, 1014,
    # 1011, 1014, 1014, 1014, 1014
    # ]

    wd_name = ["月","火","水","木","金","土","日"]

    while True:

        # 2024年11月14日(日)
        now = datetime.datetime.now()
        wd_no = now.weekday()

        # AHT,BMPの有無を確認して表示内容を変える
        # ない場合は、時計のみとする

        if THP == 1:
            mes = now.strftime("%Y年%m月%d日") + "(" + wd_name[wd_no] + ")"
            draw.text((10, 0), mes, font=ep_lib.font_set("gos", 30), fill=0)
            mes = now.strftime(" %H時%M分 ")
            draw.text((50, 40), mes, font=ep_lib.font_set("gos", 30), fill=0)

            # 気温、湿度、気圧を読み取り
            try:
                with open(path + 'temp_data_last.txt') as f:
                    temp = f.read()
                    temp = str(int(temp) /10)
                with open(path + 'humdy_data_last.txt') as f:
                    humdy = f.read()
                with open(path + 'press_data_last.txt') as f:
                    press = f.read()
                THP=1 # 計測値あり
            except:
                THP=0 # 計測値なし
        else:
            mes = now.strftime("%Y年%m月%d日") + "(" + wd_name[wd_no] + ")"
            draw.text((15, 10), mes, font=ep_lib.font_set("gos", 30), fill=0)
            mes = now.strftime("%H時%M分 ")
            draw.text((25, 60), mes, font=ep_lib.font_set("gos", 60), fill=0)


        if THP==1: # 計測値ありの場合のみ表示する
            mes = "" + temp + "度 " + humdy + "% " + press + "hPa"
            print(mes)
            # # テキストを画像に描画
            draw.text((0, 90), mes, font=ep_lib.font_set("gos", 28), fill=0)
            # ep_lib.write_buffer()
            ep_lib.ep_draw(0, 0, image, 0, 0)

            # 気圧が上昇か下降かを判定 ただし、計測開始から30分以上の経過が必要
            press = int(press)
            press_34.append(press) # 5分の移動平均を取るのに+5必要
            high_or_low = 0 # 0:不明　1:high 2:low 3:変わらず
            if len(press_34) > 34:
                press_34 = press_34[-34:]  # 一番古いデータを捨てる
                # 気圧のhigt_lowを判別
                high_or_low = press_higt_low(press_34)

            print(high_or_low)
            # 気圧の上昇・下降などを矢印で表示
            # high_or_low = 1
            if high_or_low == 0:
                image_path = path + 'bmp/空白.bmp'
            if high_or_low == 1:
                image_path = path + 'bmp/上矢印.bmp'
            if high_or_low == 2:
                image_path = path + 'bmp/下矢印.bmp'
            if high_or_low == 3:
                image_path = path + 'bmp/横棒.bmp'
            bitmap = Image.open(image_path)
            x,y = 252,90
            BorW = 0
            ep_lib.ep_draw(x,y,bitmap,BorW,1)
            # ep_lib.write_buffer()
        else:
            ep_lib.ep_draw(0, 0, image, 0, 1)

        # 描画用のオブジェクトをクリアする（白で塗りつぶす）
        draw.rectangle([0, 0, 292, 119], fill=1)

        # 正分になるのを待つ
        dt_now = datetime.datetime.now()
        while dt_now.second != 0:
            dt_now = datetime.datetime.now()
            time.sleep(0.01)

if __name__ == "__main__":
    main()
