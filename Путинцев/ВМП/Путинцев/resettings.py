import json
FILE = "settings.json"
width = 10
height = 10
mine_count = 20


def save_file():
    with open(FILE, mode='w') as fout:
        json.dump((width, height, mine_count),fout)


if __name__ == '__main__':
    save_file()
print("загрузка настроек")
print(__name__)
print("загрузка настроек завершена")