import pygame
from state import IdleState, RunningState, JumpingState
from direction_state import DirectionState, FacingRightState, FacingLeftState

class Sonic:
    def __init__(self):
        self.state = IdleState()
        self.direction_state = FacingRightState()
        self.velocity_x = 0
        self.velocity_y = 0
        self.position = [0, 500]  # Start at the very left side of the screen
        self.screen_width = 800  # Set the screen width
        self.current_level_state = None  # Track the current level state to determine ground structure

    def handle_input(self, command):
        command.execute(self)

    def update(self):
        self.state.update(self)

        # Prevent Sonic from climbing to higher ground without jumping
        if self.is_approaching_higher_ground() and not isinstance(self.state, JumpingState):
            self.velocity_x = 0
            if self.direction_state == FacingRightState():
                self.position[0] -= 1  # Step back to prevent climbing
            elif self.direction_state == FacingLeftState():
                self.position[0] += 1  # Step back to prevent climbing

        self.position[0] += self.velocity_x
        self.position[1] += self.velocity_y

        # Ensure Sonic doesn't exit the screen from the left
        if self.position[0] < 0:
            self.position[0] = 0

        # Apply gravity
        self.apply_gravity()

        # Ensure Sonic stays on the ground
        if self.is_on_ground():
            self.velocity_y = 0
            self.position[1] = self.get_ground_level() - 30  # Adjust position to stay on the ground

            # If Sonic was jumping and is now on the ground, check if he should go to idle or running
            if isinstance(self.state, JumpingState):
                if self.velocity_x == 0:
                    self.set_state(IdleState())
                else:
                    self.set_state(RunningState())

        # Check if Sonic reaches the right edge of the screen
        if self.position[0] >= self.screen_width:
            self.position[0] = 0  # Reset Sonic's position to the left side of the screen
            return "next_level"  # Return a signal to transition to the next level

    def set_state(self, state: RunningState):
        self.state = state

    def set_direction_state(self, direction_state: DirectionState):
        self.direction_state = direction_state

    def get_image(self):
        base_image = self.state.get_image(self)
        return self.direction_state.get_image(self, base_image)
    
    def apply_gravity(self):
        if not self.is_on_ground():
            self.velocity_y += 1  # Gravity effect

    def is_on_ground(self):
        ground_level = self.get_ground_level()
        return self.position[1] >= ground_level - 30  # Sonic's height is subtracted to detect the ground correctly

    def get_ground_level(self):
        return self.current_level_state.ground_level(self.position[0])

    def get_next_ground_level(self):
        """Returns the ground level for the next section Sonic would move to."""
        next_position = self.position[0] + self.velocity_x
        return self.current_level_state.ground_level(next_position)

    def is_approaching_higher_ground(self):
        """Determines if Sonic is approaching higher ground."""
        current_ground_level = self.get_ground_level()
        next_ground_level = self.get_next_ground_level()

        # Check if Sonic is moving towards a higher ground
        return next_ground_level < current_ground_level

    def handle_key_release(self):
        if self.velocity_x == 0:  # If no horizontal movement, transition to idle state
            self.set_state(IdleState())
