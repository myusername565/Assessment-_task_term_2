# The room class
class Room:
    # Initialising each room of the game
    def __init__(self, number):
        self.room_number = number
        self.neighbours = []
        self.has_pit = False
        self.has_bats = False
        self.has_wumpus = False

    # Gives each room neigbours
    def add_neighbour(self, room):
        self.neighbours.append(room)
