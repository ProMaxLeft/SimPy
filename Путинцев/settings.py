from log import select_log, log_warning
import json
select_log('saper.log')
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
except Exception as e:
    log_warning(type(e), e, sep='\n')
    save_file()


if __name__ == '__main__':
    save_file()
