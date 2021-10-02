import tkinter as tk
from PIL import Image, ImageTk
# ↓2021.09.21 Okumura
import os
import configparser
import errno
# ↑2021.09.21 Okumura
from . import Global

class Syogaibutu:

# ↓2021.09.14 Okumura
    config_ini = configparser.ConfigParser()
    config_ini_path = 'config.ini'

    # 指定したiniファイルが存在しない場合、エラー発生
    if not os.path.exists(config_ini_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(
            errno.ENOENT), config_ini_path)

    config_ini.read(config_ini_path, encoding='utf-8')

    # iniの値取得
    read_obstacle = config_ini['OBSTACLE']
    img_obstacle = read_obstacle.get('image')
    moveSize = int(read_obstacle.get('moveSize'))
    moveSpan = int(read_obstacle.get('moveSpan'))
    x = int(read_obstacle.get('x'))
    # ↑2021.09.14 Okumura

    time = 0

# def __init__(self,No, x, y, height, width):
#         self.No = No
#         self.x = x
#         self.y = y
#         self.height = height
#         self.width = width
#         self.changesize()
#         self.draw() 
#         self.leftmove()

    def __init__(self, No, y, height, width, wait):
        self.No = No
        self.y = y
        self.height = height
        self.width = width
        self.wait = wait
        self.changesize()
        self.draw() 
        self.leftmove()

    def draw(self):
        self.id = Global.cv.create_image(
            self.x, self.y, image=Global.syogaibutu_tkimg[self.No], tag="Syogaibutu")

    def changesize(self):
        # syogaibutu_img = Image.open("Image/Syogaibutu.png")
        syogaibutu_img = Image.open(self.img_obstacle)
        syogaibutu_img = syogaibutu_img.resize((self.height,self.width))
        Global.syogaibutu_tkimg.append(ImageTk.PhotoImage(syogaibutu_img))

    def leftmove(self):
        self.time = self.time+1
        print(self.id)
        print(self.time)
        print(self.wait)
        if Global.pauseText == 0 and self.time > self.wait:
            Global.cv.move(self.id,self.moveSize,0)
        Global.cv.after(self.moveSpan,self.leftmove)