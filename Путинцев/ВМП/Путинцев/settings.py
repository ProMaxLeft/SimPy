import json
FILE = "settings.json"
width = 10
height = 10
mine_count = 20


def save_file():
    with open(FILE, mode='w') as fout:
        json.dump((width, height, mine_count),fout)

try:
    with open(FILE) as fin:
        data = json.load(fin)
        width, height, mine_count = data
except:
    print("Проблемы с файлом, создаю новый")
    save_file()

if __name__ == '__main__':
    save_file()
