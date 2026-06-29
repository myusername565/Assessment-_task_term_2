import random

from map import Map
from player import Player
from wumpus import Wumpus


class Game:

    def __init__(self):
        self.map = Map()
        self.player = Player()
        self.wumpus = Wumpus()

        self.setup_game()

    def setup_game(self):

        rooms = list(self.map.rooms.values())

        random.shuffle(rooms)

        self.player.current_room = rooms.pop()

        self.wumpus.current_room = rooms.pop()
        self.wumpus.current_room.has_wumpus = True

        pit1 = rooms.pop()
        pit1.has_pit = True

        pit2 = rooms.pop()
        pit2.has_pit = True

        bat1 = rooms.pop()
        bat1.has_bats = True

        bat2 = rooms.pop()
        bat2.has_bats = True

    def show_status(self):
        room = self.player.current_room

        print(f"\nYou are in room {room.room_number}")

        print("You can move to:")
        for n in room.neighbours:
            print(f"- Room {n.room_number}")

    def check_nearby_dangers(self):
        room = self.player.current_room

        for n in room.neighbours:
            if n.has_wumpus:
                print("You smell something terrible...")
            if n.has_pit:
                print("You feel a breeze...")
            if n.has_bats:
                print("You hear flapping...")

    def move_player(self):
        choice = int(input("Enter room number to move: "))

        for n in self.player.current_room.neighbours:
            if n.room_number == choice:
                self.player.move(n)
                return

        print("Invalid move!")

    def play(self):
        while self.player.is_alive:

            self.show_status()
            self.check_nearby_dangers()

            action = input("\n(M)ove or (Q)uit: ").lower()

            if action == "m":
                self.move_player()
            elif action == "q":
                break
            else:
                print("Invalid input!")