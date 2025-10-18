# Minimax Tic-Tac-Toe

An unbeatable Tic-Tac-Toe AI implementation using the Minimax algorithm with Alpha-Beta pruning optimization.

## Features

- **Perfect AI**: Never loses, plays optimally using game theory
- **Minimax Algorithm**: Explores all possible game states
- **Alpha-Beta Pruning**: Optimizes search by eliminating unnecessary branches
- **Clean Interface**: Simple text-based gameplay

## How to Run

```bash
python tictactoe_game.py
```

## Game Rules

- You play as **X**, AI plays as **O**
- Enter moves using numbers 1-9 corresponding to board positions:
```
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
```

## Algorithm Overview

### Minimax
- **Recursive search** through all possible game states
- **MAX player** (AI) maximizes score
- **MIN player** (Human) minimizes score
- **Scoring**: +1 (AI win), -1 (AI loss), 0 (draw)

### Alpha-Beta Pruning
- **Optimization** of Minimax algorithm
- **Prunes branches** that won't affect final decision
- **Same result** as Minimax but faster execution

## Code Structure

- `LINES`: Winning combinations (rows, columns, diagonals)
- `winner()`: Detects game winner
- `moves()`: Returns available positions
- `terminal()`: Checks if game is over
- `utility()`: Scores terminal states
- `minimax()`: Basic Minimax implementation
- `alphabeta()`: Optimized version with pruning
- `play_game()`: Main game loop

## Learning Objectives

✅ Adversarial search and Minimax algorithm  
✅ Game state evaluation (terminal tests & utility)  
✅ Recursive Minimax agent implementation  
✅ Alpha-beta pruning optimization  
✅ Optimal play and search complexity analysis

## Requirements

- Python 3.9+
- No external dependencies

## Author

France Rivera - UPHSL CCS J3A