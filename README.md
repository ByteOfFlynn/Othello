# Othello (Command-Line Logic Engine)

This project implements a fully interactive, command-line version of the board logic for **Othello** (Reversi), a deterministic, turn-based piece-capturing system. Built in Python, the engine encapsulates rule enforcement, board management, and turn-based piece flipping logic, all without relying on any graphics or external libraries.

Although the core mechanic resembles a game, this project is structured more as a rule-based system that demonstrates board sorting, directional search algorithms, and data-state transformations through a consistent API.

## Features

- 8x8 internal board representation with boundary padding
- Valid move detection and automatic turn passing when no moves are available
- Real-time piece flipping based on directional chain detection
- Accurate end-game evaluation and piece counting
- CLI interface with a clean, readable board state output

## How It Works

### Game Rules Modeled

- Pieces are flipped when captured across a continuous straight line (horizontal, vertical, or diagonal).
- Players alternate turns; if no valid move exists, the turn is skipped.
- The game ends when neither player can make a valid move.
- The winner is the player with the most pieces at game end.

### Board Representation

- Internally stored as a 10x10 2D list:
  - `*` = edge boundary
  - `.` = empty playable space
  - `X` = black piece
  - `O` = white piece

### Move Handling

- All move validation and execution logic is encapsulated in:
  - `return_available_positions(color)`
  - `make_move(color, position)`
  - `play_game(color, position)`

These methods handle full directional scanning, piece flipping, and post-move board state updates.

## Example Usage

```python
game.print_board()
game.play_game("black", (6, 5))
game.print_board()
game.play_game("white", (6, 6))
game.print_board()
```

## Example Output
```python
* * * * * * * * * *
* . . . . . . . . *
* . . . . . . . . *
* . . . O X . . . *
* . . . X O . . . *
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* * * * * * * * * *

