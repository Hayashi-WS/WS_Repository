import tkinter as tk
from PIL import Image, ImageTk
# ↓2021.09.21 Okumura
import os
import configparser
import errno
# ↑2021.09.21 Okumura
from . import Global

class Obstacle:

# ↓2021.09.14 Okumura
    #config_ini = configparser.ConfigParser()
    #config_ini_path = 'Setting/Obstacle_1.ini'

    # 指定したiniファイルが存在しない場合、エラー発生
    #if not os.path.exists(config_ini_path):
    #    raise FileNotFoundError(errno.ENOENT, os.strerror(
    #        errno.ENOENT), config_ini_path)

    #config_ini.read(config_ini_path, encoding='utf-8')

    # iniの値取得
    #read_obstacle = config_ini['OBSTACLE']
    #img_obstacle = read_obstacle.get('image')
    #moveSize = int(read_obstacle.get('moveSize'))
    #moveSpan = int(read_obstacle.get('moveSpan'))
    #x = int(read_obstacle.get('x'))
    # ↑2021.09.14 Okumura

    #time = 0

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
        self.setteingGet()
        self.No = No
        self.y = y
        self.height = height
        self.width = width
        self.wait = wait
        self.changesize()
        self.draw() 
        self.leftmove()

    def setteingGet(self):
        config_ini = configparser.ConfigParser()
        # 選択したマップ番号に応じて読み込むファイルを決定
        config_ini_path = 'Setting/Obstacle_' + str(Global.mapNum) + '.ini'

        # 指定したiniファイルが存在しない場合、エラー発生
        if not os.path.exists(config_ini_path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(
                errno.ENOENT), config_ini_path)

        config_ini.read(config_ini_path, encoding='utf-8')

        # iniの値取得
        read_obstacle = config_ini['OBSTACLE']
        self.img_obstacle = read_obstacle.get('image')
        self.moveSize = int(read_obstacle.get('moveSize'))
        self.moveSpan = int(read_obstacle.get('moveSpan'))
        self.x = int(read_obstacle.get('x'))

    def draw(self):
        self.id = Global.cv.create_image(
            self.x, self.y, image=Global.obstacle_tkimg[self.No], tag="Obstacle")

    def changesize(self):
        # syogaibutu_img = Image.open("Image/Syogaibutu.png")
        obstacle_img = Image.open(self.img_obstacle)
        obstacle_img = obstacle_img.resize((self.height,self.width))
        Global.obstacle_tkimg.append(ImageTk.PhotoImage(obstacle_img))

    def leftmove(self):
        if Global.pauseText == 0 and Global.globalTime > self.wait:
            Global.cv.move(self.id,self.moveSize,0)
        Global.cv.after(self.moveSpan,self.leftmove)