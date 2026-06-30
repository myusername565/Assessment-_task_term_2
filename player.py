class Player:
    def __init__(self):
        self.current_room = None
        self.arrows = 2
        self.is_alive = True

    def move(self, room):
        self.current_room = room
