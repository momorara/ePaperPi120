#!/usr/bin/python
"""
2025/01/18
もとのoPaperのライブラリはbitmapフォントを使用するもので、bdfparserを使うものとなっている。
それだと、pipでのインストールが必要となりbookwormでは仮想環境が必要となる
そのためbdfparserを使わない方法として、TrueTypeのみを使うこととした。
しかし、TrueTypeをつかって、元のライブラリと共存させようとするとePaperの縦横がおかしくなる。
そこで、TrueTypeを使う場合は、ImageDraw.Draw(image)上の領域に文字と図形を全て書きePaperに
転送することで、表示することとする。
なので、文字も図形もImageDraw クラスのメソッドを使うことにする。
ただし、ePaperの初期化、転送のみ元のライブラリを使うこととなる。
"""
import ep_lib
import time

def main():

    print("画面を初期化して、白くする。")
    draw,image = ep_lib.image_set()
    ep_lib.clear_w(draw)
    dy = 0 #6
    draw.text((0, 0+dy) ,"今回はご購入", font=ep_lib.font_set("gos",24) ,fill=0)  # 0は黒
    draw.text((0, 26+dy) ," ありがとうございました。", font=ep_lib.font_set("gos",24) ,fill=0)  # 0は黒
    draw.text((0, 57+dy) ,"サポートページ", font=ep_lib.font_set("gos",20) ,fill=0)  # 0は黒
    draw.text((0, 80+dy) ,"github.com/momorara/ePaperPi120", font=ep_lib.font_set("gos",16) ,fill=0)  # 0は黒
    draw.text((0, 102+dy) ,"をご確認ください。TKJ-Works川端", font=ep_lib.font_set("gos",18) ,fill=0)  # 0は黒

    ep_lib.ep_draw(0,0,image,0,1)
    
    # SPI を終了（リソースを解放）
    ep_lib.close()

if __name__ == '__main__':
    main()
