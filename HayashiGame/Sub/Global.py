import tkinter as tk
# ↓2021.09.08 Hayashi
# from PIL import Image, ImageTk
# import random
# ↑2021.09.08 Hayashi
from . import Kao

WINDOW_HEIGHT = 600  # ウィンドウの高さ
WINDOW_WIDTH = 1000   # ウィンドウの幅

TEXT_PAUSE_SIZE = 40

cv:tk.Canvas
# ↓2021.09.08 Hayashi
# kao_tkimg:ImageTk.PhotoImage
# ↑2021.09.08 Hayashi
root:tk.Tk

kao:Kao

btn:tk.Button
pauseText = 999
startFlag = False

#↓小林追記20210905--------------------------------------
obstacle_tkimg = []
obstacle = []
#↑小林追記20210905--------------------------------------

globalTime = 0
mapNum = 0

def pause(event):
    global pauseText
    if pauseText != 999:
        if pauseText != 0:
            cv.delete(pauseText)
            pauseText = 0
        else:
            pauseText = cv.create_text(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, text="PAUSE",
                        fill="red", font=("System", TEXT_PAUSE_SIZE))


def left_click(event):
    if pauseText == 0 and kao.moveStop == False:
        kao.moveStop = True
        kao.jump()

def timeStart():
    global globalTime
    if pauseText == 0:
        globalTime += 1
    root.after(1000, timeStart)