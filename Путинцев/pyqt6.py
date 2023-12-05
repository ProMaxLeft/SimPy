from game import Game
from PyQt6.QtWidgets import *


#создание приложения 
app = QApplication([])
import sprites 

#Создание окна
window = QWidget()
label_mines = QLabel(window)
button_main = QPushButton('@', window)
buttons = []

#запуск
def run(game: Game):
    PX_CELL = 32
    PX_BORDER = PX_CELL // 3
    PX_TOP = PX_CELL * 3 // 2
    PX_WIDTH = PX_BORDER * 2 + game.width * PX_CELL
    PX_HEIGHT = PX_BORDER * 3 + PX_TOP + game.heigth * PX_CELL

    window.setGeometry(100, 100, PX_WIDTH, PX_HEIGHT)

    label_mines.setText(str(game.mines))
    label_mines.setGeometry(PX_BORDER, PX_BORDER, PX_TOP * 2, PX_TOP)
    
    button_main.setGeometry(
        (PX_WIDTH - PX_TOP) // 2, PX_BORDER, PX_TOP, PX_TOP)
   
    buttons.clear()
    for x in range(game.width):
        new_column = []
        for y in range(game.heigth):
            new_button = QPushButton(sprites.)
            new_button.setGeometry(PX_BORDER + x * PX_CELL, 2 * PX_BORDER + PX_TOP + y * PX_CELL, PX_CELL, PX_CELL)
            new_column.append(new_button)
        buttons.append(new_column)    



    window.show()
    app.exec()


if __name__ == "__main__":
    run(Game(5, 4, 3))