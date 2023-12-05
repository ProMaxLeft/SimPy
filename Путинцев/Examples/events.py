class Event:
    def __init__(self, action):
        self.action = action

    def check(self):
        return True
    
    def try_fire(self):
        if self.check():
            self.action()
            return True
        return False

class TimerEvent(Event):
    timer = 0
    @classmethod
    def advance(cls, time):
        cls.timer += time
    
    def __init__(self, time, action):
        super().__init__(action)
        self.time = self.timer + time

    def check(self):
        return self.timer >= self.time


class KeyboardEvent(Event):
    def check(self):
        return # нажата ли клавиша