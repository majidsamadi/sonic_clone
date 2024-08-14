import pygame
import time

class SonicState:
    def update(self, sonic):
        pass

    def get_image(self, sonic):
        pass

class IdleState(SonicState):
    def __init__(self):
        self.timer = time.time()
        self.image_index = 0

    def update(self, sonic):
        elapsed_time = time.time() - self.timer
        if elapsed_time < 10:  # 10 seconds
            self.image_index = 0
        elif elapsed_time < 11:  # 1 second
            self.image_index = 1
        elif elapsed_time < 12:  # 1 second
            self.image_index = 2
        else:
            self.timer = time.time()  # Reset the timer after cycling through images

    def get_image(self, sonic):
        return [pygame.image.load(f'assets/images/sonic/idle{i}.png') for i in range(1, 4)][self.image_index]

class RunningState(SonicState):
    run_images = [pygame.image.load(f'assets/images/sonic/run{i}.png') for i in range(1, 5)]

    def __init__(self):
        self.timer = time.time()
        self.image_index = 0

    def update(self, sonic):
        elapsed_time = time.time() - self.timer
        if elapsed_time > 0.05:  # 50 milliseconds for each frame
            self.image_index = (self.image_index + 1) % len(self.run_images)
            self.timer = time.time()  # Reset the timer for the next frame

    def get_image(self, sonic):
        return self.run_images[self.image_index]

class JumpingState(SonicState):
    def __init__(self):
        self.jump_up_image = pygame.image.load('assets/images/sonic/jumpup.png')
        self.jump_down_image = pygame.image.load('assets/images/sonic/jumpdown.png')
        self.jumping_up = True

    def update(self, sonic):
        if sonic.velocity_y < 0:
            self.jumping_up = True
        else:
            self.jumping_up = False

    def get_image(self, sonic):
        return self.jump_up_image if self.jumping_up else self.jump_down_image
