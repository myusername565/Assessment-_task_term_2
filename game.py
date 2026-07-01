# importing other codes from other files into this file
import random
from map import Map
from player import Player
from wumpus import Wumpus


# The main game class
class Game:

    # initialising the class
    def __init__(self):
        self.map = Map()
        self.player = Player()
        self.wumpus = Wumpus()

        self.setup_game()

    # creating the pre-game logic
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

    # checking for player death
    def check_current_room(self):
        room = self.player.current_room

        # Wumpus
        if room.has_wumpus:
            print("\n💀 The Wumpus ate you!")
            self.player.is_alive = False

        # Pit
        if room.has_pit:
            print("\n🕳 You fell into a pit!")
            self.player.is_alive = False

        # Bats
        if room.has_bats:
            print("\n🦇 Super bats picked you up!")

            possible_rooms = [r for r in self.map.rooms.values() if r != room]

            self.player.current_room = random.choice(possible_rooms)

            print(f"You were dropped into Room {self.player.current_room.room_number}")

            # Check the new room immediately
            self.check_current_room()

            return

    # displaying the neccessary information for the player
    def show_status(self):
        room = self.player.current_room

        print("\n==============================")
        print(f"You are in Room {room.room_number}")
        print(f"Arrows Remaining: {self.player.arrows}")

        print("\nConnected Rooms:")
        for neighbour in room.neighbours:
            print(f"Room {neighbour.room_number}")

    # displaying nearbye danger/warnings to the player
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
        print("==============================")
        print("      HUNT THE WUMPUS")
        print("==============================")
        print("Kill the Wumpus before it kills you.")
        print("Beware of pits and super bats!")
        print()
        while self.player.is_alive:

            self.show_status()
            self.check_nearby_dangers()

            self.check_current_room()

            if not self.player.is_alive:
                break

            action = input("\n(M)ove or (S)hoot or (Q)uit: ").lower()

            if action == "m":
                self.move_player()

            elif action == "s":
                self.shoot_arrow()

            elif action == "q":
                break

            else:
                print("Invalid input!")

            if self.wumpus.is_alive and not self.player.is_alive:
                print("\n==========")
                print("GAME OVER")
                print("==========")
            elif not self.wumpus.is_alive:
                print("\n===================")
                print("YOU KILLED THE WUMPUS!")
                print("YOU WIN!")
                print("===================")
                break

    def shoot_arrow(self):

        if self.player.arrows == 0:
            print("You have no arrows left!")
            self.player.is_alive = False
            return

        target = int(input("Shoot into which room? "))

        valid_room = False

        for neighbour in self.player.current_room.neighbours:

            if neighbour.room_number == target:

                valid_room = True

                self.player.arrows -= 1

                if neighbour.has_wumpus:
                    print("\n🏹 Your arrow hit the Wumpus!")
                    print("YOU WIN!")

                    self.wumpus.is_alive = False
                    return

                print("Missed!")

                return

        if not valid_room:
            print("You can only shoot into an adjacent room.")
