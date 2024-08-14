import pygame
from sonic import Sonic
from level_state import Level1State
from controller import Controller
from enemy import RedEnemy, PurpleEnemy
from collectible import GoldCollectible, SilverCollectible
from state import JumpingState  # Import JumpingState

class GameFacade:
    def __init__(self):
        self.sonic = Sonic()
        self.current_background = None
        self.current_level_state = None
        self.clock = pygame.time.Clock()
        self.next_level_state = None
        self.controller = Controller(self.sonic)  # Pass sonic to the controller

        # Initialize enemies and collectibles
        self.enemies = [RedEnemy([0, 470]), PurpleEnemy([0, 470])]
        self.collectibles = [GoldCollectible([300, 470]), SilverCollectible([500, 470])]

    def start_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Sonic Game")
        initial_level = Level1State()
        initial_level.load_level(self)
        self.current_level_state = initial_level  # Set the initial level state explicitly
        self.sonic.current_level_state = initial_level  # Ensure Sonic knows the current level state
        self.game_loop()

    def game_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Quit event detected.")
                else:
                    running = self.controller.handle_input(event)
                    print(f"Event handled: {event}, Running: {running}")

            if self.sonic.update() == "next_level":
                self.next_level_state = self.current_level_state.next_level
                print("Next level triggered.")

            if self.next_level_state:
                self.next_level_state.load_level(self)
                self.current_level_state = self.next_level_state
                self.sonic.current_level_state = self.next_level_state
                self.next_level_state = None
                print(f"Loaded next level: {self.current_level_state}")

            # Update and draw enemies and collectibles
            for enemy in self.enemies:
                enemy.update(self.current_level_state.ground_level)  # Pass ground level function
                enemy.draw(self.screen)
                
                # Check for collision with Sonic
                if self.check_collision(self.sonic, enemy):
                    if not isinstance(self.sonic.state, JumpingState):
                        print("Game Over! Sonic collided with an enemy.")
                        self.display_game_over_screen()
                        running = False  # End the game loop

            for collectible in self.collectibles:
                collectible.draw(self.screen)
                if collectible.collect(self.sonic.position):
                    self.collectibles.remove(collectible)
                    print("Collectible collected.")

            self.render()
            self.clock.tick(60)

        pygame.quit()
        print("Game exited.")




    def check_collision(self, sonic, enemy):
        sonic_rect = pygame.Rect(sonic.position[0], sonic.position[1], 30, 30)  # Assuming Sonic's size is 30x30
        enemy_rect = pygame.Rect(enemy.position[0], enemy.position[1], 30, 30)  # Assuming Enemy's size is 30x30
        return sonic_rect.colliderect(enemy_rect)

    def display_game_over_screen(self):
        self.screen.fill((255, 255, 255))  # White background
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (0, 0, 0))  # Black text
        text_rect = text.get_rect(center=(400, 300))  # Center the text on the screen
        self.screen.blit(text, text_rect)
        pygame.display.flip()

        # Wait for a few seconds before quitting
        pygame.time.wait(3000)

    def render(self):
        self.screen.fill((255, 255, 255))
        
        if self.current_background:
            self.screen.blit(self.current_background, (0, 0))
        
        # Draw collectibles before Sonic to ensure they are not overlapped by anything else
        for collectible in self.collectibles:
            collectible.draw(self.screen)
        
        # Draw Sonic
        sonic_image = self.sonic.get_image()
        self.screen.blit(sonic_image, (self.sonic.position[0], self.sonic.position[1]))

        # Draw enemies after Sonic so they appear in the foreground
        for enemy in self.enemies:
            enemy.draw(self.screen)

        pygame.display.flip()
