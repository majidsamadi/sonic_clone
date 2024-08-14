from abc import ABC, abstractmethod
import pygame

class DirectionState(ABC):
    @abstractmethod
    def get_image(self, sonic, base_image):
        pass

class FacingRightState(DirectionState):
    def get_image(self, sonic, base_image):
        return base_image  # No flipping needed, already facing right

class FacingLeftState(DirectionState):
    def get_image(self, sonic, base_image):
        return pygame.transform.flip(base_image, True, False)  # Flip the image horizontally
