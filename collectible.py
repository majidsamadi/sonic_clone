import pygame
from abc import ABC, abstractmethod

class CollectibleInterface(ABC):
    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def collect(self, player_position):
        pass


class GoldCollectible(CollectibleInterface):
    def __init__(self, position):
        self.position = position
        self.image = pygame.image.load('assets/images/collectible/collectible1.png')
        print(f"GoldCollectible image size: {self.image.get_size()}")  # Debugging line

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def collect(self, player_position):
        collectible_rect = pygame.Rect(self.position, (20, 20))  # Updated size to match the image size
        player_rect = pygame.Rect(player_position, (30, 30))  # Assuming Sonic's size is 30x30
        if collectible_rect.colliderect(player_rect):
            print("Gold collected!")
            return True
        return False

class SilverCollectible(CollectibleInterface):
    def __init__(self, position):
        self.position = position
        self.image = pygame.image.load('assets/images/collectible/collectible2.png')
        print(f"SilverCollectible image size: {self.image.get_size()}")  # Debugging line

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def collect(self, player_position):
        collectible_rect = pygame.Rect(self.position, (20, 20))  # Updated size to match the image size
        player_rect = pygame.Rect(player_position, (30, 30))  # Assuming Sonic's size is 30x30
        if collectible_rect.colliderect(player_rect):
            print("Silver collected!")
            return True
        return False
