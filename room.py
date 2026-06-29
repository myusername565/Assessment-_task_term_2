class Room:
    def __init__(self, number):
        self.room_number = number
        self.neighbours = []
        self.has_pit = False
        self.has_bats = False
        self.has_wumpus = False

    def add_neighbour(self, room):
        self.neighbours.append(room)
