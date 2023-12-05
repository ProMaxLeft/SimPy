from time import sleep
from events import TimerEvent
FPS = 10
interval = 1 / FPS

frame_count = 0

actions = []

def onTime():
    print("Время пришло!")
    actions.append(duringTime)

def duringTime():
    print("Работаем!")

def onTime2():
    print("Время ушло!")
    actions.clear()

events = []
events.append(TimerEvent(1, onTime))
events.append(TimerEvent(2, onTime2))

while True:
    # отчёты
    print(frame_count, 'frame')

    # события
    i = 0
    while i < len(events):
        if events[i].try_fire():
            events.pop(i)
        else:
            i += 1

    # обработка
    for action in actions:
        action()

    # fps
    sleep(interval)
    frame_count += 1
    TimerEvent.advance(interval)
