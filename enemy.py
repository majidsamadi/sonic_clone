import pygame
from abc import ABC, abstractmethod
from direction_state import FacingRightState, FacingLeftState

class Enemy(ABC):
    def __init__(self, position):
        self.position = position
        self.velocity_x = 1  # Horizontal movement speed
        self.velocity_y = 0  # Vertical movement speed
        self.direction_state = FacingRightState()  # Start by facing right
        self.current_image = None
        self.height = 30  # Enemy height
        self.image_index = 0

    @abstractmethod
    def load_images(self):
        pass

    def update(self, ground_level_func):
        # Determine the current and next ground levels
        current_ground_level = ground_level_func(self.position[0])
        next_x = self.position[0] + self.velocity_x
        next_ground_level = ground_level_func(next_x)

        # Check if the enemy should change direction at the edges or higher ground
        if next_x <= 0 or next_x >= 770 or next_ground_level < current_ground_level:
            # Change direction at the screen edges or when encountering higher ground
            self.change_direction()
            return
            
        # Move horizontally if not stuck at the edges
        self.position[0] += self.velocity_x

        # Apply gravity if moving toward lower ground
        if self.position[1] < next_ground_level - self.height:
            self.velocity_y += 1  # Apply gravity to fall down
        else:
            self.velocity_y = 0  # Stop falling if on the ground

        # Apply vertical movement (falling)
        self.position[1] += self.velocity_y

        # Ensure the enemy doesn't fall below the ground level
        if self.position[1] > next_ground_level - self.height:
            self.position[1] = next_ground_level - self.height

        # Update the image for animation
        self.update_image()

    def change_direction(self):
        self.velocity_x = -self.velocity_x
        if isinstance(self.direction_state, FacingRightState):
            self.direction_state = FacingLeftState()
        else:
            self.direction_state = FacingRightState()

    def update_image(self):
        # Update the image based on direction
        base_image = self.images[self.image_index]
        self.current_image = self.direction_state.get_image(self, base_image)

    def draw(self, screen):
        screen.blit(self.current_image, self.position)


class RedEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position)
        self.images = self.load_images()
        self.current_image = self.images[0]
        self.image_timer = 0
        self.image_index = 0

    def load_images(self):
        return [
            pygame.image.load('assets/images/enemy/enemy_red1.png'),
            pygame.image.load('assets/images/enemy/enemy_red2.png')
        ]

    def update_image(self):
        elapsed_time = pygame.time.get_ticks()
        if elapsed_time - self.image_timer > 1000:  # Change image every 1 second
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image_timer = elapsed_time

        super().update_image()


class PurpleEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position)
        self.images = self.load_images()
        self.current_image = self.images[0]
        self.image_timer = 0
        self.image_index = 0

    def load_images(self):
        return [
            pygame.image.load('assets/images/enemy/enemy_purple1.png'),
            pygame.image.load('assets/images/enemy/enemy_purple2.png')
        ]

    def update_image(self):
        elapsed_time = pygame.time.get_ticks()
        if elapsed_time - self.image_timer > 1000:  # Change image every 1 second
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image_timer = elapsed_time

        super().update_image()
