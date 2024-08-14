class Sonic:
    def __init__(self):
        self.speed = 5

    def get_speed(self):
        return self.speed

class SpeedDecorator:
    def __init__(self, sonic):
        self.sonic = sonic

    def get_speed(self):
        return self.sonic.get_speed() + 10
