from PyQt6.QtWidgets import *

app = QApplication([])
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
window = MainWindow()
scene = QGraphicsScene(0, 0, 800, 600 ,window)
view = QGraphicsView(scene, window)
view.setGeometry(0, 0, 810, 610)

def run():
    window.show()
    app.exec()

if __name__ == "__main__":
    run()