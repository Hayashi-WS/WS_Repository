# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import ImageTk, Image

import Lib

import Sub


def btn_click():
    btn.place_forget()
    Sub.Global.pauseText = 0


if __name__ == "__main__":
    # 初期描画
    Sub.Global.root = tk.Tk()
    Sub.Global.root.title("HayashiGame")
    Sub.Global.cv = tk.Canvas(Sub.Global.root, width=Sub.Global.WINDOW_WIDTH, height=Sub.Global.WINDOW_HEIGHT, bg="black")
    Sub.Global.cv.bind('<Button-1>', Sub.Global.left_click)
    Sub.Global.cv.bind('<Button-3>', Sub.Global.pause)
    Sub.Global.cv.pack()

    # 画像の読み込み
    # 奧村追記: try catch
    # 今後、関数化予定
    # 0902奥村尚樹
    # try:
    #     kao_img = Image.open("Image\\hayashi_kao.jpeg")
    # except:
    #     kao_img = Image.open("Image/hayashi_kao.jpeg")
    # 0902奥村尚樹

    # 0906奥村尚樹
    # imageトライキャッチを関数化
    # 好きな変数名 = x_image("windowsパス","macパス")
    kao_img = Image.open("Image/hayashi_kao.jpeg")
    # 0906奥村尚樹

    Sub.Global.kao_tkimg = ImageTk.PhotoImage(kao_img)

    # メニューバー
    menubar = tk.Menu(Sub.Global.root)
    Sub.Global.root.configure(menu=menubar)
    menubar.add_command(label="QUIT", underline=0, command=Sub.Global.root.quit)

    # ボタン
    btn = tk.Button(Sub.Global.root, text='START', width=20, height=5, command=btn_click)
    btn.place(x=430, y=200)

    # インスタンス生成
    Sub.Global.kao = Sub.Kao.Kao(100, Sub.Global.WINDOW_HEIGHT - 30)

    Sub.Global.root.mainloop()