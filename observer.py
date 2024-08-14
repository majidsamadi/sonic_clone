class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

class Level(Subject):
    def __init__(self):
        super().__init__()
        self.completed = False

    def complete(self):
        self.completed = True
        self.notify_observers()

class GameObserver:
    def update(self):
        print("Level completed!")
