from abc import ABC, abstractmethod
from state import RunningState, JumpingState, IdleState
from direction_state import FacingRightState, FacingLeftState

class Command(ABC):
    @abstractmethod
    def execute(self, sonic):
        pass

class MoveRightCommand(Command):
    def execute(self, sonic):
        sonic.velocity_x = 5
        sonic.set_direction_state(FacingRightState())
        sonic.set_state(RunningState())

class MoveLeftCommand(Command):
    def execute(self, sonic):
        sonic.velocity_x = -5
        sonic.set_direction_state(FacingLeftState())
        sonic.set_state(RunningState())

class JumpCommand(Command):
    def execute(self, sonic):
        if sonic.is_on_ground():  # Ensure Sonic can only jump if he's on the ground
            sonic.velocity_y = -12
            sonic.set_state(JumpingState())

class StopCommand(Command):
    def execute(self, sonic):
        sonic.velocity_x = 0
        if not isinstance(sonic.state, JumpingState):
            sonic.set_state(IdleState())
