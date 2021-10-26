import tkinter as tk
from PIL import Image, ImageTk
import os
import configparser
import errno
from . import Global
import Lib

class Obstacle:

    # コンストラクタ
    def __init__(self, No):
        self.No = No
        self.settingGet()
        self.changesize()
        self.draw() 
        self.leftmove()

    # 外部パラメータ取得
    def settingGet(self):
        iniPath = 'Setting/Obstacle_' + str(Global.mapNum) + '.ini'
        section = 'OBSTACLE_' + str(self.No+1)
        self.img_obstacle = Lib.IniLib.iniSettingGet(iniPath, section, 'image', False)
        self.moveSize = Lib.IniLib.iniSettingGet(iniPath, section, 'moveSize', True)
        self.moveSpan = Lib.IniLib.iniSettingGet(iniPath, section, 'moveSpan', True)
        self.x = Lib.IniLib.iniSettingGet(iniPath, section, 'x', True)
        self.y = Lib.IniLib.iniSettingGet(iniPath, section, 'y', True)
        self.width = Lib.IniLib.iniSettingGet(iniPath, section, 'width', True)
        self.height = Lib.IniLib.iniSettingGet(iniPath, section, 'height', True)
        self.wait = Lib.IniLib.iniSettingGet(iniPath, section, 'wait', True)

    # オブジェクト描画
    def draw(self):
        self.id = Global.cv.create_image(self.x, self.y, image=Global.obstacle_tkimg[self.No], tag="Obstacle")

    # オブジェクトサイズ調整
    def changesize(self):
        obstacle_img = Image.open(self.img_obstacle)
        obstacle_img = obstacle_img.resize((self.width, self.height))
        Global.obstacle_tkimg.append(ImageTk.PhotoImage(obstacle_img))

    # オブジェクト左移動
    def leftmove(self):
        if Global.pauseText == 0 and Global.globalTime > self.wait:
            Global.cv.move(self.id, self.moveSize, 0)
        Global.cv.after(self.moveSpan,self.leftmove)