# ↓2021.09.08 Hayashi
from PIL import ImageTk, Image
import os
# ↑2021.09.08 Hayashi
# ↓2021.09.14 Okumura
import configparser
import errno
# ↑2021.09.14 Okumura
from . import Global


class Kao:

    # ↓2021.09.14 Okumura
    config_ini = configparser.ConfigParser()
    config_ini_path = 'Setting/config.ini'

    # 指定したiniファイルが存在しない場合、エラー発生
    if not os.path.exists(config_ini_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(
            errno.ENOENT), config_ini_path)

    config_ini.read(config_ini_path, encoding='utf-8')

    # iniの値取得
    read_character = config_ini['CHARACTER']
    jumpSize = int(read_character.get('jumpSize'))
    jumpCnt = int(read_character.get('jumpCnt'))
    jumpSpan = int(read_character.get('jumpSpan'))
    image_kao = read_character.get('image')

    moveSize = int(read_character.get('moveSize'))
    moveSpan = int(read_character.get('moveSpan'))
    # ↑2021.09.14 Okumura

    jumpMax = False 
    moveStop = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.leftRight = 1
        self.draw()
        self.leftRight_Move()

    def draw(self):
        # ↓2021.09.08 Hayashi
        # self.id = Global.cv.create_image(
        #     self.x, self.y, image=Global.kao_tkimg, tag="kao")
        # os.path.joinを使えばOSに依存せずにパスの指定が可能

        kao_img = Image.open(self.image_kao)
        # PhotoImageオブジェクトを参照し続けるために、グローバル変数にしないといけない
        global kao_tkimg
        kao_tkimg = ImageTk.PhotoImage(kao_img)
        self.id = Global.cv.create_image(
            self.x, self.y, image=kao_tkimg, tag="kao")
        # ↑2021.09.08 Hayashi

    def leftRight_Move(self):
        if Global.pauseText == 0 and self.moveStop == False:
            Global.cv.move(self.id, Kao.moveSize * self.leftRight, 0)
            self.x += Kao.moveSize * self.leftRight
            self.leftRight *= -1
        Global.root.after(self.moveSpan, self.leftRight_Move)

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
            self.moveStop = False
