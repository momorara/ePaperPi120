"""
2025/03/04  ePaper用のアプリとして、天気予報を表示する。
            openweathermapからAPIで天気予報データを取得して、表示する。
            openweathermapの子予報は3時間毎だが、一応毎正時にePaperは書き換える。
            1回実行のみとして、cronで起動させる方法とした。

            cronで
            0 * * * * sleep 10 && python3 /home/pi/ePaperPi/Weather_one.py
            などとしてください。

2025/03/06  サンプルとして、APIキーを載せていますが、予告なしに停止する予定です。
            使用し続けるためにはご自身でAPIキーを取得してください。
            お住まいの近くのデータはご自身で設定してください。
2025/03/09  あるかもしれない天気を追加　雷　霧
"""

import requests
from datetime import datetime
import time
import ep_lib

# OpenWeatherMap APIの設定
"""
APIはサインインして
https://home.openweathermap.org/api_keys
にて取得。
"""
API_KEY = "7944259d800fa4c97ba44d2bd029e6fd"  # APIキーを取得して入力 test
CITY = "Tokyo"
CITY = "Otaru,jp"
CITY = "Neyagawa,jp"
# CITY = "Fukuoka"
# CITY = "Kagoshima-ken"
# CITY = "City of London"
# CITY = "Greenland"
# CITY = "New York City"
# CITY = "Peru"
# CITY = "Kiefen"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric&lang=ja"

"""
天気の種類
晴　雨　曇　雪　雹

ただし直近の3時間はそのまま表示

小雨 厚い雲
雲　雨　雨　雨　
"""

def get_weather():
    """3時間ごとの天気予報を取得して表示"""
    response = requests.get(URL)

    w_list=[]
    w_list_no=[]
    
    if response.status_code == 200:
        data = response.json()
        forecasts = data["list"]
        
        print(f"都市: {CITY} の3時間ごとの天気予報")
        print("=" * 40)

        # 3時間ごとのデータから3時間ごとのデータを取得
        for i in range(0, len(forecasts), 1):  #  (3時間間隔なので1,6時間ごとなら2ステップ)
            dt_txt = forecasts[i]["dt_txt"]  # 日時
            # temp = forecasts[i]["main"]["temp"]  # 気温
            weather = forecasts[i]["weather"][0]["description"]  # 天気
            # humidity = forecasts[i]["main"]["humidity"]  # 湿度
            # wind_speed = forecasts[i]["wind"]["speed"]  # 風速
            
            dt = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
            # print(f"{dt.strftime('%H')} {weather}")
            w_list.append(f"{weather}")  # 時間を数字でリストにする
            w_list_no.append(int(dt.strftime('%H'))) #時間に対応した天気をリスト化する 
            # print(f"  気温: {temp}°C  天気: {weather}")
            # print(f"  天気: {weather}")
            # print(f"  湿度: {humidity}%")
            # print(f"  風速: {wind_speed}m/s")
            if i > 38: # max 38
                print("=" * 0)
                break
    else:
        print("天気情報の取得に失敗しました。")
        w_list_no,w_list = -1,"*"
    return w_list_no,w_list


def weather_check():
    # 実行
    w_list_no,w_list = get_weather()
    print(w_list_no)
    print(w_list)

    # 今の時間を求める
    now = datetime.now()
    print("今の時間",now.hour)
    now_hour = now.hour // 3
    print("天気予報の時間の位置",now_hour)
    # 天気予報時間を位置から求める
    w_hour_list = [0,3,6,9,12,15,18,21,0]
    w_hour = w_hour_list[now_hour]
    print("今の時間の天気予報の時間",w_hour)
    now_w_point= w_list_no.index(w_hour)
    print("今の時間の天気予報の位置",now_w_point)
    # 今の天気予報を求める
    now_weather = w_list[now_w_point]
    print("今の時間の天気予報",now_weather)
    print("次の3時間の天気予報",w_list[now_w_point+1])
    print("")
    print("次の3時間の天気予報",w_list[now_w_point+2])
    print("次の3時間の天気予報",w_list[now_w_point+3])
    print("次の3時間の天気予報",w_list[now_w_point+4])
    print("次の3時間の天気予報",w_list[now_w_point+5])
    print("次の3時間の天気予報",w_list[now_w_point+6])
    print("次の3時間の天気予報",w_list[now_w_point+7])

    return w_hour,w_list,now_w_point


# 単純化した天気を求める
def weathe_Simplify(weather):
    #晴　雨　曇　雪　雹 に単純化する
    w_simple_list = ["晴","雨","雲","雪","雹","曇","雷","霧","no"]
    result = -1
    for i in range(len(w_simple_list)):
        result = weather.find(w_simple_list[i])
        if result != -1:
            result = i
            break
    # print(result,w_simple_list[result] )
    return w_simple_list[result] 


draw, image = ep_lib.image_set()  # eペーパーディスプレイ用の描画オブジェクトと画像を取得
# ePaper 表示準備
ep_lib.clear_w(draw)  # 画面を白でクリア


# 天気予報情報の取得
w_hour,w_list,now_w_point = weather_check()

# 表示文字を作って表示
mes = str(w_hour) + "時        3時間後"
draw.text((15, 10), mes, font=ep_lib.font_set("gos", 20), fill=0)
mes = w_list[now_w_point]
draw.text((0, 36), mes, font=ep_lib.font_set("gos", 32), fill=0)
mes = w_list[now_w_point+1]
draw.text((130, 36), mes, font=ep_lib.font_set("gos", 32), fill=0)

# 単純化した天気
mes ="後3時間毎:"
for i in range(2,7):
    result = weathe_Simplify(w_list[now_w_point+i])
    mes = mes + result + " " 
print(mes)
draw.text((0, 90), mes, font=ep_lib.font_set("gos", 24), fill=0)

# 実際にePaperに書き込む
ep_lib.ep_draw(0, 0, image, 0, 1)
