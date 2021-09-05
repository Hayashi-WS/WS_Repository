import tkinter as tk
from PIL import Image, ImageTk
from . import Global

class Syogaibutu:


    def __init__(self,No, x, y, height, width):
        self.No = No
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.changesize()
        self.draw() 
        self.leftmove()

    def draw(self):
        self.id = Global.cv.create_image(
            self.x, self.y, image=Global.syogaibutu_tkimg[self.No], tag="Syogaibutu")

    def changesize(self):
        try:
            syogaibutu_img = Image.open("Image\\Syogaibutu.png")
        except:
            syogaibutu_img = Image.open("Image/Syogaibutu.png")
        syogaibutu_img = syogaibutu_img.resize((self.height,self.width))
        Global.syogaibutu_tkimg.append(ImageTk.PhotoImage(syogaibutu_img))

    def leftmove(self):
        if Global.pauseText == 0:
            Global.cv.move(self.id,-5,0)
        Global.cv.after(3,self.leftmove)