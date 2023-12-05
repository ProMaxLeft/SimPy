from PyQt6.QtGui import QColor
from PyQt6.QtCore import QTimer
import window
class Character1:
    size = 100
    def __init__(self, name, x, y):
        self.rect = window.scene.addRect(x, y, self.size, self.size)
        self.text = window.scene.addText(name)
        self.text.setPos(x, y)
        self.setColor(0, 0, 255)

    def setColor(self, r, g, b):
        self.rect.setPen(QColor(r, g, b))
        self.rect.setBrush(QColor((255*3 + r) // 4, (255*3 + g) // 4, (255*3 + b) // 4))
        self.text.setDefaultTextColor(QColor(r,g,b))
    
    def move(self, dx, dy):
        self.rect.moveBy(1,0)
        self.text.moveBy(1,0)

class Character2:
    size = 100
    def __init__(self, name, x, y):
        self.rect = window.scene.addRect(x, y, self.size, self.size)
        self.text = window.scene.addText(name)
        self.text.setPos(x, y)
        self.setColor(0, 128, 0)

    def setColor(self, r, g, b):
        self.rect.setPen(QColor(r, g, b))
        self.rect.setBrush(QColor((255*3 + r) // 4, (255*3 + g) // 4, (255*3 + b) // 4))
        self.text.setDefaultTextColor(QColor(r,g,b))

vasya = Character1("Vasya", 100, 100)
masha = Character2("Masha", 200, 200)

FPS = 60

def update():
    vasya.move(1, 0)

timer = QTimer(window.window)
timer.timeout.connect(update)
timer.start(1000 // FPS)
window.run()