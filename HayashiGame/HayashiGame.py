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

    # メニューバー
    menubar = tk.Menu(Sub.Global.root)
    Sub.Global.root.configure(menu=menubar)
    menubar.add_command(label="QUIT", underline=0, command=Sub.Global.root.quit)

    # ボタン
    btn = tk.Button(Sub.Global.root, text='START', width=20, height=5, command=btn_click)
    btn.place(x=430, y=200)

    # インスタンス生成
    Sub.Global.kao = Sub.Kao.Kao(100, Sub.Global.WINDOW_HEIGHT - 30)

    #↓小林追記20210905-------------------------------------------------
    # mapファイル的なものを設定して障害物の配列等を入れておく
    # Sub.Global.syogaibutu = [Sub.Syogaibutu.Syogaibutu(0, 0, 600, 10000, 10),

    #                         Sub.Syogaibutu.Syogaibutu(1, 1150, 570, 200, 200),
    #                         Sub.Syogaibutu.Syogaibutu(2, 2000, 570, 500, 200),
    #                         Sub.Syogaibutu.Syogaibutu(3, 2750, 570, 1000, 400)]
    #↑小林追記20210905-------------------------------------------------

        # mapファイル的なものを設定して障害物の配列等を入れておく
    Sub.Global.syogaibutu = [Sub.Syogaibutu.Syogaibutu(0, 600, 10000, 10, 0),

                            Sub.Syogaibutu.Syogaibutu(1, 570, 200, 200, 100),
                            Sub.Syogaibutu.Syogaibutu(2, 570, 500, 200, 1000),
                            Sub.Syogaibutu.Syogaibutu(3, 570, 1000, 400, 2000)]

    Sub.Global.root.mainloop()