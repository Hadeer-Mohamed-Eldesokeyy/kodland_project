# Forest Escape

Forest Escape is a simple 2D platformer game built with Python using Pygame Zero.

The main goal is to make your way to the flag at the top of the level. You need to jump between platforms, avoid enemies, and make sure you do not fall off the screen.

## About the Game

The player starts at the bottom of the level and has to work their way up by jumping across different platforms. There are two enemies in the level, a zombie and a soldier, each moving within its own area.

If the player touches an enemy or falls off the screen, the game is over. Reaching the flag means you win.

## Controls

| Key                     | Action               |
| ----------------------- | -------------------- |
| Left / Right Arrow Keys | Move left or right   |
| Space                   | Jump                 |
| Mouse                   | Use the menu buttons |

## Features

The game includes:

* A main menu with Start, Sound, and Exit buttons
* Player movement and jumping
* Platform collisions
* Two different enemies
* Enemy patrol movement
* Idle and walking animations
* Background music
* Sound effects for jumping, getting hit, and winning
* Win and lose conditions

## How to Run

First, make sure Python is installed on your computer.

Then install Pygame Zero:

```bash id="80o2fc"
pip install pgzero
```

Open a terminal in the project folder and run:

```bash id="ztue3m"
pgzrun game.py
```

Make sure the `images`, `sounds`, and `music` folders are in the same project directory so the game can load all the required assets.

## Project Structure

```text id="ojz91t"
game_project/
│
├── game.py
├── README.md
│
├── images/
│   ├── Player and enemy sprites
│   └── Flag image
│
├── sounds/
│   ├── jump.ogg
│   ├── hit.ogg
│   └── win.ogg
│
└── music/
    └── theme.ogg
```

## Technologies Used

This project was built using:

* Python
* Pygame Zero
* `pygame.Rect` for collision detection

No other external libraries are used.

## Code Structure

The game uses classes to organize the characters and their behavior.

The `Character` class contains the shared animation logic.

The `Player` class handles movement, jumping, gravity, and collisions with the platforms.

The `Enemy` class controls enemy movement and keeps each enemy inside its assigned patrol area.

The rest of the code handles the level setup, enemies, menu buttons, game states, and the main Pygame Zero functions.

## Assets

The game assets used in this project come from Kenney and are available under the CC0 license.

Kenney: https://kenney.nl
