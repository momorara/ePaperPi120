"""
2025/01/19
ポモドーロ・タイマー

timer=5 
time_multiplier=60
としたら5分タイマーになります。
"""
timer=5
time_multiplier = 60 # 1:1秒　60:1分

import ep_lib
import time

def draw_frame(draw, x0, y0, width, height, num_frames):
    """
    外枠と均等に配置された内枠を描画します。
    パラメータ:
        draw: 図形を描画するための描画オブジェクト。
        x0, y0: 外枠の左上の座標。
        width, height: 外枠の幅と高さ。
        num_frames: 内枠の数。
    """
    # 各内枠の幅を計算します。'4' を2回引くのは、パディングと外枠の幅を考慮するためです。
    d_width = int((width - 4 - 4) / num_frames)
    # 外枠を描画します。
    draw.rectangle((x0, y0, x0 + width, y0 + height - 2), outline="black", fill="white", width=1)
    # 各内枠を描画します。
    for i in range(num_frames):
        x = (x0 + 2) + d_width * i + i * 2  # 現在の内枠の左上のx座標を計算します。
        draw.rectangle((x, y0 + 2, x + d_width, y0 + height - 4), outline="black", fill="white", width=1)

def fill_frame(draw, x0, y0, d_width, height, n):
    """
    指定されたインデックスに基づいて内枠を塗りつぶします。
    パラメータ:
        draw: 図形を描画するための描画オブジェクト。
        x0, y0: 外枠の左上の座標。
        d_width: 各内枠の幅。
        height: 内枠の高さ。
        n: 塗りつぶす内枠のインデックス (0から始まる)。
    """
    # 塗りつぶす枠の左上の座標を計算します。
    xn = (x0 + 2) + d_width * n + n * 2
    yn = y0 + 2
    # 徐々に小さくなる矩形で枠を塗りつぶします。
    for i in range(d_width // 4):
        width_n  = d_width - i * 2
        height_n = height - 4 - i * 2  # '4' を引くのは上下のパディングを考慮するためです。
        draw.rectangle((xn + i * 2, yn + i * 2, xn + width_n, yn + height_n), outline="black", fill="white", width=1)

def main():

    print("画面を初期化して、白くする。")
    draw, image = ep_lib.image_set()  # eペーパーディスプレイ用の描画オブジェクトと画像を取得
    ep_lib.clear_w(draw)  # 画面を白でクリア

    # タイマーのタイトルテキストを描画
    draw.text((0, 0), "5-minute timer", font=ep_lib.font_set("gos", 22), fill=0)
    x0, y0 = 0, 25
    width, height = 288, 102  # 外枠の幅と高さ
    num_frames = 5  # タイマーの進行を表す内枠の数
    # 外枠と内枠を描画
    draw_frame(draw, x0, y0, width, height, num_frames)
    # ep_lib.write_buffer()
    ep_lib.ep_draw(0, 0, image, 0, 1)
    # 各内枠の幅を再計算
    d_width = int((width - 4 - 4) / num_frames)


    # 各内枠を順番に塗りつぶしてタイマーの進行を表現
    for n in range(num_frames):
        time.sleep(timer * time_multiplier)  # 各枠に対して1秒の遅延をシミュレート
        fill_frame(draw, x0, y0, d_width, height, n)
        # ep_lib.write_buffer()
        ep_lib.ep_draw(0, 0, image, 0, 1)


    # 全ての枠が塗りつぶされた後に "Time UP" メッセージを表示の準備
    time.sleep(1)
    text = "Time UP"
    font = ep_lib.font_set("gos", 48)
    # テキストのサイズと中央揃えの位置を計算
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    center_x = (width - text_width) // 2
    center_y = (height - text_height) // 2 + y0
    # "Time UP" メッセージ用の白い背景を描画し、その上にテキストを描画
    draw.rectangle((center_x - 10, center_y - 10, center_x + text_width + 10, center_y + text_height + 20), fill="white", outline="black")
    draw.text((center_x, center_y), text, font=font, fill=0)
    # ep_lib.write_buffer()
    ep_lib.ep_draw(0, 0, image, 0, 1)

if __name__ == '__main__':
    main()
