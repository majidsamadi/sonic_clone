import pygame
from abc import ABC, abstractmethod

class LevelState(ABC):
    def __init__(self):
        self.level_number = 0
        self.next_level = None

    @abstractmethod
    def load_level(self, game_facade):
        pass

    def ground_level(self, position):
        return 500

class Level1State(LevelState):
    def __init__(self):
        super().__init__()
        self.level_number = 1

    def load_level(self, game_facade):
        print("Loading Level 1...")
        game_facade.sonic.position = [0, 500]  # Sonic starts on the ground
        game_facade.sonic.current_level = 1
        game_facade.current_background = pygame.image.load('assets/images/backgrounds/level1.png')

        # Set the next level
        self.next_level = Level2State()

        # Position enemies on the ground level away from Sonic
        start_x_positions = [400, 600]  # Set initial x-positions for enemies
        for i, enemy in enumerate(game_facade.enemies):
            enemy.position = [start_x_positions[i], self.ground_level(start_x_positions[i]) - 30]  # Adjust for enemy height

    def ground_level(self, position):
        return 500

class Level2State(LevelState):
    def __init__(self):
        super().__init__()
        self.level_number = 2

    def load_level(self, game_facade):
        print("Loading Level 2...")
        game_facade.sonic.position = [0, 500]
        game_facade.sonic.current_level = 2
        game_facade.current_background = pygame.image.load('assets/images/backgrounds/level2.png')

        # Set the next level
        self.next_level = Level3State()

        # Position enemies on the ground level away from Sonic
        start_x_positions = [400, 600]  # Set initial x-positions for enemies
        for i, enemy in enumerate(game_facade.enemies):
            enemy.position = [start_x_positions[i], self.ground_level(start_x_positions[i]) - 30]  # Adjust for enemy height

    def ground_level(self, position):
        if position < 400:
            return 500
        else:
            return 470

class Level3State(LevelState):
    def __init__(self):
        super().__init__()
        self.level_number = 3

    def load_level(self, game_facade):
        print("Loading Level 3...")
        game_facade.sonic.position = [0, 500]
        game_facade.sonic.current_level = 3
        game_facade.current_background = pygame.image.load('assets/images/backgrounds/level3.png')

        # Set the next level
        self.next_level = Level4State()

        # Position enemies on the ground level away from Sonic
        start_x_positions = [400, 600]  # Set initial x-positions for enemies
        for i, enemy in enumerate(game_facade.enemies):
            enemy.position = [start_x_positions[i], self.ground_level(start_x_positions[i]) - 30]  # Adjust for enemy height

    def ground_level(self, position):
        if position < 200:
            return 500
        elif position < 400:
            return 470
        else:
            return 440

class Level4State(LevelState):
    def __init__(self):
        super().__init__()
        self.level_number = 4

    def load_level(self, game_facade):
        print("Loading Level 4...")
        game_facade.sonic.position = [0, 500]
        game_facade.sonic.current_level = 4
        game_facade.current_background = pygame.image.load('assets/images/backgrounds/level4.png')

        # Set the next level
        self.next_level = Level1State()  # Loop back to Level 1

        # Position enemies on the ground level away from Sonic
        start_x_positions = [400, 600]  # Set initial x-positions for enemies
        for i, enemy in enumerate(game_facade.enemies):
            enemy.position = [start_x_positions[i], self.ground_level(start_x_positions[i]) - 30]  # Adjust for enemy height

    def ground_level(self, position):
        if position < 200:
            return 440
        elif position < 400:
            return 470
        elif position < 600:
            return 500
        else:
            return 470
