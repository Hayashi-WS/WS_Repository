import tkinter as tk
import re
from PIL import ImageTk, Image
import Lib
import Sub

# グローバルで宣言しておかないと、以下の各関数内で同じオブジェクトの操作ができない
startBtn:tk.Button

def map_select(event):
    global startBtn
    mapText = event.widget.cget("text")
    # ボタンテキストの数字部分を抽出
    Sub.Global.mapNum = re.sub(r"\D", "", mapText)
    mapBtn1.place_forget() # 即席で一個ずつ消す方法で実装
    mapBtn2.place_forget()
    # マップを選択したらスタートボタン表示
    startBtn = tk.Button(Sub.Global.root, text='START', width=20, height=5, command=btn_click)
    startBtn.place(x=430, y=200)

def btn_click():
    global startBtn
    startBtn.place_forget()
    # マップ番号が確定してから障害物のオブジェクト作成

    # マップファイルを読み込む
    # 障害物の数、サイズ出現時間を読み込んで、その設定値によってインスタンスを作成

    Sub.Global.obstacle = [Sub.Obstacle.Obstacle(0, 600, 10000, 10, 0), # wait秒数もiniファイルから取得するようにしないといけない
                            Sub.Obstacle.Obstacle(1, 570, 200, 200, 2),
                            Sub.Obstacle.Obstacle(2, 570, 500, 200, 5),
                            Sub.Obstacle.Obstacle(3, 570, 1000, 400, 7)]
    Sub.Global.pauseText = 0
    Sub.Global.timeStart()


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

    # マップボタン
    # 1
    mapBtn1 = tk.Button(Sub.Global.root, text='MAP 1', width=20, height=2)
    mapBtn1.place(x=50, y=50)
    mapBtn1.bind("<ButtonPress>", map_select)
    # 2
    mapBtn2 = tk.Button(Sub.Global.root, text='MAP 2', width=20, height=2)
    mapBtn2.place(x=50, y=95)
    mapBtn2.bind("<ButtonPress>", map_select)

    # スタートボタン
    #btn = tk.Button(Sub.Global.root, text='START', width=20, height=5, command=btn_click)
    #btn.place(x=430, y=200)

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
    #Sub.Global.obstacle = [Sub.Obstacle.Obstacle(0, 600, 10000, 10, 0),
    #                        Sub.Obstacle.Obstacle(1, 570, 200, 200, 2),
    #                        Sub.Obstacle.Obstacle(2, 570, 500, 200, 5),
    #                        Sub.Obstacle.Obstacle(3, 570, 1000, 400, 7)]

    Sub.Global.root.mainloop()