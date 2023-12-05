import datetime
log_path = 'log.log'

def log(info,*args, sep=', '):
    time = datetime.datetime.now()
    with open(log_path, mode ='a') as fout:
        print(f"[{time}] {info}", *args, file=fout, sep=sep)

def log_warning(info, *args, sep=', '):
    log(f'[warn] {info}', *args, sep=sep)

def select_log(path):
    global log_path
    log_path = path
    with open(log_path, mode='w'):
        pass
    log("Старт лога")



if __name__ == "__main__":
    select_log(log_path)