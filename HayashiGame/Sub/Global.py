import tkinter as tk
from . import Gorilla

WINDOW_HEIGHT = 600  # ウィンドウの高さ
WINDOW_WIDTH = 1000   # ウィンドウの幅

TEXT_PAUSE_SIZE = 40

cv:tk.Canvas
root:tk.Tk

gorilla:Gorilla

btn:tk.Button
pauseText = 999
startFlag = False

obstacle_tkimg = []

globalTime = 0
mapNum = 0

# 一時停止時の処理
def pause(event):
    global pauseText
    # スタート前でない
    if pauseText != 999:
        # 既に一時停止中の場合は再開処理
        if pauseText != 0:
            cv.delete(pauseText)
            pauseText = 0
        # 一時停止中でない場合は一時停止処理
        else:
            pauseText = cv.create_text(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, text="PAUSE",
                        fill="red", font=("System", TEXT_PAUSE_SIZE))

# 左クリック押下時のジャンプ処理
def left_click(event):
    # スタートボタン押下前でない、かつ一時停止中でない、かつジャンプ中でない場合はジャンプ処理実施
    if pauseText == 0 and gorilla.nowJump == False:
        gorilla.nowJump = True
        gorilla.jump()

# グローバルタイム更新処理
def timeStart():
    global globalTime
    # 動作中の場合のみタイム更新
    if pauseText == 0:
        globalTime += 1
    root.after(1000, timeStart)