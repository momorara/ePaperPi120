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

    draw.text((0, 0) ,"日本語　ゴシック", font=ep_lib.font_set("gos",24) ,fill=0)  # 0は黒
    draw.text((0, 26) ,"日本語　明朝", font=ep_lib.font_set("min",30) ,fill=0)  # 0は黒
    draw.text((0, 57) ,"abcdefghijkl 0123456789", font=ep_lib.font_set("gos",20) ,fill=0)  # 0は黒
    draw.text((0, 77) ,"0123456789 abcdefghijkl", font=ep_lib.font_set("gos",24) ,fill=0)  # 0は黒
    draw.text((0, 102) ,"!#$%&'()+*<>?/.,", font=ep_lib.font_set("gos",20) ,fill=0)  # 0は黒

    ep_lib.ep_draw(0,0,image,0,1)
    time.sleep(5)
    ep_lib.clear_w(draw)

if __name__ == '__main__':
    main()
