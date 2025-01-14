# Tic-Tac-Toe Game

## Overview
A Python Tic-Tac-Toe game with three modes:
+ Player vs Computer
+ Player vs Player
+ Computer vs Computer

Tracks statistics and includes AI for challenging gameplay.

## Features
- **Modes**: Player vs Computer, Player vs Player, Computer vs Computer
- **AI**: Smart moves for competitive play
- **Statistics**: Tracks wins, losses, and draws
- **Easy Interface**: Clear prompts and tabulated board

## Requirements
- Python 3.6+
- Install Tabulate: `pip install tabulate`

## How to Play
1. **Player vs Computer**: Select `1`, choose ❌ or ⭕, and take turns. Align three marks to win.
2. **Player vs Player**: Select `2` and alternate turns.
3. **Computer vs Computer**: Select `3` to watch AI play.

### Run the Game
```bash
python xox_game.py
```
## AI Strategy
+ Win if possible
+ Block opponent’s win
+ Prioritize center or corners
+ Random move as a last resort

## Board Layout
``` 
  1 | 2 | 3
  ---------
  4 | 5 | 6
  ---------
  7 | 8 | 9
```
## Key Functions
+ Places a mark on the board
+ Checks for a winner
+ Detects a draw
+ Implements AI logic
+ Selects the game mode
+ Displays game stats
## Future Enhancements
+ Add difficulty levels
+ Create a GUI
+ Enable online multiplayer

## License
Open-source under MIT License.
