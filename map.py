# importing data from other files
from room import Room
from Map_data import connections


# The map class
class Map:
    # initialising the class
    def __init__(self):
        self.rooms = {}

        for i in range(1, 13):
            self.rooms[i] = Room(i)

        self.create_connections()

    # creating the connections and giving every room 3 neighbours
    def create_connections(self):

        for room_number, neighbours in connections.items():
            room = self.rooms[room_number]

            for neighbour in neighbours:
                room.add_neighbour(self.rooms[neighbour])
