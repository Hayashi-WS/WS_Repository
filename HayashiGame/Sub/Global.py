import tkinter as tk
from PIL import Image, ImageTk
import random
import Sub.Kao
import Sub.Syogaibutu


WINDOW_HEIGHT = 600  # ウィンドウの高さ
WINDOW_WIDTH = 1000   # ウィンドウの幅

TEXT_PAUSE_SIZE = 40


cv:tk.Canvas
kao_tkimg:ImageTk.PhotoImage
root:tk.Tk

kao:Sub.Kao

btn:tk.Button
pauseText = 999
startFlag = False

#小林追記--------------------------------------
syogaibutu_tkimg = []
syogaibutu = []
#小林追記--------------------------------------


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