# Hunt the Wumpus (Python OOP)

## Overview

Hunt the Wumpus is a text-based adventure game developed using Object-Oriented Programming (OOP) principles in Python. The player explores a cave made up of connected rooms while attempting to locate and defeat the Wumpus using a limited number of arrows. Along the way, the player must avoid dangerous hazards such as bottomless pits and giant bats.

The game focuses on strategic movement, exploration, and decision-making while demonstrating core OOP concepts such as classes, objects, encapsulation, and interaction between multiple game components.

---

## Features

- Object-Oriented Python implementation
- Randomly generated cave hazards
- Connected room navigation
- Wumpus AI movement (if implemented)
- Hazard warning system
- Limited arrows for attacking
- Win and lose conditions
- Input validation
- Replay option (if implemented)

---

## Game Rules

1. The player starts in a random safe room.
2. The cave consists of interconnected rooms.
3. One room contains the Wumpus.
4. Some rooms contain bottomless pits.
5. Some rooms contain giant bats.
6. Entering a room with:
   - The Wumpus results in defeat.
   - A pit causes the player to fall and lose.
   - Giant bats transport the player to another random room.
7. The player receives warnings when hazards are nearby.
8. The player can:
   - Move to an adjacent room.
   - Shoot an arrow into an adjacent room.
9. If the arrow hits the Wumpus, the player wins.
10. Missing the shot may cause the Wumpus to move (depending on implementation).

---

## Controls

### Move

```
m
```

Choose one of the connected rooms.

### Shoot

```
s
```

Choose an adjacent room to fire an arrow.

### Quit

```
q
```

Ends the game.

---

## Project Structure

```
HuntTheWumpus/
│
├── main.py
├── player.py
├── room.py
├── map.py
├── wumpus.py
├── game.py
├── Map_data.py
└── README.md
```
---

## Classes

Typical classes used include:

- `Game` – Controls the game loop and overall gameplay.
- `Player` – Stores player position, arrows, and actions.
- `Room` – Represents individual cave rooms.
- `map` – Creates and connects the cave layout.
- `Wumpus` – Handles the Wumpus behaviour.
- `Map_data` – Represents room connections on the map

---

## Requirements

- Python 3.10 or newer

---

## Running the Game

1. Open a terminal.
2. Navigate to the project folder.

Run:

```bash
python main.py
```

or

```bash
python3 main.py
```

depending on your operating system.

---

## OOP Concepts Demonstrated

This project demonstrates:

- Classes and Objects
- Encapsulation
- Composition
- Object Interaction
- Methods
- Constructors
- Data Abstraction

---

## Winning

The player wins by successfully shooting the Wumpus before running out of arrows or encountering a deadly hazard.

---

## Losing

The player loses if:

- They enter the Wumpus's room.
- They fall into a pit.
- They run out of arrows.

---

## Author
Yousef R.
Created as a school project to demonstrate Object-Oriented Programming in Python.
