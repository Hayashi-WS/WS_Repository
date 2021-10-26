from PIL import ImageTk, Image
import os
import configparser
import errno
from . import Global
import Lib


class Gorilla:

    jumpMax = False
    nowJump = False # ジャンプ処理中はTrue

    # コンストラクタ
    def __init__(self, x, y):
        self.settingGet()
        self.x = x
        self.y = y
        self.leftRight = 1
        self.draw()
        self.leftRight_Move()

    # 外部パラメータ取得
    def settingGet(self):
        iniPath = 'Setting/config.ini'
        section = 'CHARACTER'
        self.jumpSize = Lib.IniLib.iniSettingGet(iniPath, section, 'jumpSize', True)
        self.jumpCnt = Lib.IniLib.iniSettingGet(iniPath, section, 'jumpCnt', True)
        self.jumpSpan = Lib.IniLib.iniSettingGet(iniPath, section, 'jumpSpan', True)
        self.image_gorilla = Lib.IniLib.iniSettingGet(iniPath, section, 'image', False)
        self.moveSize = Lib.IniLib.iniSettingGet(iniPath, section, 'moveSize', True)
        self.moveSpan = Lib.IniLib.iniSettingGet(iniPath, section, 'moveSpan', True)

    # オブジェクト描画
    def draw(self):
        gorilla_img = Image.open(self.image_gorilla)
        gorilla_img = gorilla_img.resize((100,100))
        # PhotoImageオブジェクトを参照し続けるために、グローバル変数にしないといけない
        global gorilla_tkimg
        gorilla_tkimg = ImageTk.PhotoImage(gorilla_img)
        self.id = Global.cv.create_image(
            self.x, self.y, image=gorilla_tkimg, tag="gorilla")

    # 左右に動作
    def leftRight_Move(self):
        # 一時停止中でなくジャンプ中でもない場合のみ処理
        if Global.pauseText == 0 and self.nowJump == False:
            Global.cv.move(self.id, self.moveSize * self.leftRight, 0)
            self.x += self.moveSize * self.leftRight
            self.leftRight *= -1
        Global.root.after(self.moveSpan, self.leftRight_Move)

    # ジャンプ処理
    def jump(self):
        # 10→1の10回分 上へ移動
        if self.jumpCnt > 0 and self.jumpMax == False:
            Global.cv.move(self.id, 0, self.jumpSize * self.jumpCnt)
            self.y += self.jumpSize * self.jumpCnt
            self.jumpCnt -= 1
        # 0→9の10回分 下へ移動
        else:
            self.jumpMax = True
            self.jumpCnt += 1
            Global.cv.move(self.id, 0, -1 * self.jumpSize * self.jumpCnt)
            self.y += -1 * self.jumpSize * self.jumpCnt

        if self.jumpCnt != 10:
            Global.root.after(self.jumpSpan, self.jump)
        # カウンタが10になった=地面に着地したらループを終了
        else:
            self.jumpMax = False
            self.nowJump = False
