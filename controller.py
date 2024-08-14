import pygame
from command import MoveRightCommand, MoveLeftCommand, JumpCommand, StopCommand

class Controller:
    def __init__(self, sonic):
        self.sonic = sonic

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.sonic.handle_input(MoveRightCommand())
            elif event.key == pygame.K_LEFT:
                self.sonic.handle_input(MoveLeftCommand())
            elif event.key == pygame.K_SPACE:
                self.sonic.handle_input(JumpCommand())
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                self.sonic.handle_input(StopCommand())
        elif event.type == pygame.QUIT:
            return False  # Return False to exit the game

        return True  # Keep running the game
