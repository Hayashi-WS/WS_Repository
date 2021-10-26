import tkinter as tk
import re
from PIL import ImageTk, Image
import Lib
import Sub

# グローバルで宣言しておかないと、以下の各関数内で同じオブジェクトの操作ができない
startBtn:tk.Button

# マップ選択後の処理
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

# スタートボタン押下時の処理
def btn_click():
    global startBtn
    startBtn.place_forget()
    
    # 外部パラメータから作成しないといけない障害物の数を取得する
    iniPath = 'Setting/Obstacle_' + str(Sub.Global.mapNum) + '.ini'
    section = 'OBSTACLE_NUM'
    obstacleNum = Lib.IniLib.iniSettingGet(iniPath, section, 'num', True)

    # 障害物インスタンスを必要な数だけ作成する
    for cnt in range(obstacleNum):
        Sub.Obstacle.Obstacle(cnt)
    
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

    # インスタンス生成
    Sub.Global.gorilla = Sub.Gorilla.Gorilla(100, Sub.Global.WINDOW_HEIGHT - 52)

    Sub.Global.root.mainloop()