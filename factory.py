class GameObjectFactory:
    @staticmethod
    def create_game_object(type, position):
        if type == "enemy":
            return Enemy(position)
        elif type == "collectible":
            return Collectible(position)
        # Add other types as needed
        return None

class Enemy:
    def __init__(self, position):
        self.position = position

class Collectible:
    def __init__(self, position):
        self.position = position
