# FOREST ESCAPE

## ABOUT THE GAME

Forest Escape is a small platformer game made with Pygame Zero.

The goal is to reach the flag at the top of the level. The player needs
to jump across the platforms while avoiding the zombie and the soldier.
The game ends if the player touches an enemy or falls off the screen.

Controls:

Left / Right arrow keys - Move
Space - Jump
Mouse - Use the menu buttons

## HOW TO RUN THE GAME

1. Make sure Python is installed.

2. Install Pygame Zero:

   pip install pgzero

3. Open the project folder and run:

   pgzrun game.py

The images, sounds and music should already be inside their folders.

## LIBRARIES USED

The project uses:

* Pygame Zero
* pygame.Rect

Rect is only imported for collision detection, which is allowed in the
project requirements.

No other external libraries are used.

## GAME FEATURES

The game includes:

* A main menu
* Start Game button
* Sound on/off button
* Exit button
* A player that can move and jump
* Platforms
* Two different enemies
* Enemies that patrol in their own areas
* Idle and walking animations
* Background music
* Jump, hit and win sounds
* A win condition when the player reaches the flag
* A lose condition when the player touches an enemy or falls

## FILES AND FOLDERS

game_project/

```
game.py
readme.txt

images/
    Player and enemy sprites
    Flag image

sounds/
    jump.ogg
    hit.ogg
    win.ogg

music/
    theme.ogg
```

## ASSETS

The images, sounds and music used in this project are from Kenney.

Website:
https://kenney.nl

The assets are free to use under the CC0 license.

## CODE STRUCTURE

The game uses classes for the characters and their animations.

The Character class contains the shared animation code.

The Player class handles player movement, jumping, gravity and platform
collisions.

The Enemy class handles enemy movement inside a specific patrol area.

The rest of the code creates the level, enemies, menu buttons and the
main Pygame Zero functions.