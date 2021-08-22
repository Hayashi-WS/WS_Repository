from . import Global

class Kao:
    jumpSize = -5
    jumpCnt = 10
    jumpSpan = 10
    jumpMax = False

    moveSize = 30
    moveSpan = 800

    moveStop = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.leftRight = 1
        self.draw()
        self.leftRight_Move()

    def draw(self):
        self.id = Global.cv.create_image(
            self.x, self.y, image=Global.kao_tkimg, tag="kao")

    def leftRight_Move(self):
        if Global.pauseText == 0 and self.moveStop == False:
            Global.cv.move(self.id, Kao.moveSize * self.leftRight, 0)
            self.x += Kao.moveSize * self.leftRight
            self.leftRight *= -1
        Global.root.after(self.moveSpan, self.leftRight_Move)

    def jump(self):
        if self.jumpCnt > 0 and self.jumpMax == False:
            Global.cv.move(self.id, 0, self.jumpSize * self.jumpCnt)
            self.y += self.jumpSize * self.jumpCnt
            self.jumpCnt -= 1
        else:
            self.jumpMax = True
            self.jumpCnt += 1
            Global.cv.move(self.id, 0, -1 * self.jumpSize * self.jumpCnt)
            self.y += -1 * self.jumpSize * self.jumpCnt
        if self.jumpCnt != 10:
            Global.root.after(self.jumpSpan, self.jump)
        else:
            self.jumpMax = False
            self.moveStop = False