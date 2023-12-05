from game import Game, MINE, CLOSED


def run(game:Game):
    is_active = True
    while is_active:
        show(game)
        line = input("Ваш ход:")
        if line == '0':
            is_active = False
        try:
            x, y = map(int, line.split())
        except:
            print("Ошибка")
            continue
        game.step(x, y)

def show(game:Game):
    for row in range(game.heigth):
        for col in range(game.width):
            e = game.field[col][row]
            print(
                '*' if e == MINE else
                '_' if e == CLOSED else
                e, end = '')
        print()