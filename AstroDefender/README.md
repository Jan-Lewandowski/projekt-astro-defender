# AstroDefender

AstroDefender is a single-player game created in Pygame, where the player takes on the role of a defender of a space base against incoming waves of enemy ships.

## How to run it?

To run the game, follow these steps:

1. **Install Python** (version 3.8 or newer is required). You can check your Python version by typing in the terminal:
	```sh
	python --version
	```

2. **Install Pygame**, if you do not have it yet:
	```sh
	pip install pygame
	```

3. **Clone the repository**:
	```sh
	git clone https://gitlab.com/ug_jn/wst-p-do-programowania-2024/grupa-3-lg/jan-lewandowski.git
	```

4. **Run the game**:
	```sh
	python main.py
	```

## Game rules

- The goal of the game is to defend the base from attacking enemy waves, which become more numerous over time. The player's objective is to get as many points as possible.
- Every hit from an enemy costs the player one life. Every meteor hit costs three lives, and every bomb hit ends the game immediately. The game ends when the player's lives drop to zero.
- Starting from level three, bonuses begin to appear, each worth three points. Starting from level five, hearts begin to appear, each adding one health point to the player.
- The player gets one point for every enemy hit.

## Additionally

- Every game score is saved in the scoreboard.
- The player can mute/unmute music and sound effects in the options.

## Controls

- **W/S/A/D (up/down/left/right)** – ship movement.
- **Space** – shoot.
- **P/O** - pause and resume gameplay
- **M** - mute/unmute music
- **N** - mute/unmute sound effects
