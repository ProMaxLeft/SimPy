import random
CLOSED = 9
MINE = 10

class Game:
    def __init__(self, width, heigth, mines):
        width = max(1, width)
        heigth = max(1, heigth)
        mines = min(mines, width * heigth - 1)
        self.width = width
        self.heigth = heigth
        self.mines = mines
        self.field = [
            [CLOSED for _ in range(heigth)]
             for _ in range(width)]
        while mines > 0:
            x = random.randint(0, width - 1)
            y = random.randint(0, heigth - 1)
            if self.field[x][y] == CLOSED:
                self.field[x][y] = MINE
                mines -= 1
        print(self.field)

    def step(self, x, y):
     self.field[x][y] = 0