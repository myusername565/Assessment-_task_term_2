# The player class
class Player:
    # Initialising the class
    def __init__(self):
        self.current_room = None
        self.arrows = 2
        self.is_alive = True

    # Moving through the map
    def move(self, room):
        self.current_room = room
