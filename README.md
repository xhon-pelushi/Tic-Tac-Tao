# Tic-Tac-Tao 🎮

A colorful, user-friendly terminal-based Tic-Tac-Toe game written in Python.

## Features ✨

### Enhanced User Experience
- **Clear visual layout** with numbered grid positions (1-9) for easy input
- **Colorful interface** with ANSI color codes:
  - Player X appears in **red**
  - Player O appears in **green**
  - Game messages are color-coded for better readability
- **Screen clearing** between moves for a clean gaming experience
- **Improved input validation** with helpful error messages
- **Position reference guide** displayed alongside the current board
- **Play again option** after each game

### Game Features
- Two-player gameplay (X and O)
- Win condition detection (rows, columns, diagonals)
- Draw condition detection
- Input validation and error handling
- Turn-based gameplay with clear player indicators

## How to Play 🎯

1. Run the game: `python3 tictactoe.py`
2. Players take turns choosing positions 1-9:
   ```
   Position Reference:
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```
3. Player X goes first (displayed in red)
4. Player O goes second (displayed in green)
5. First player to get three in a row wins!
6. Choose to play again or exit after each game

## Requirements 📋

- Python 3.x
- Terminal with ANSI color support (most modern terminals)

## Recent Improvements 🚀

- Added numbered position system (1-9) instead of row/column coordinates
- Implemented colorful output using ANSI escape sequences
- Enhanced visual layout with reference grid
- Improved error messages and input validation
- Added screen clearing for better UX
- Added welcome messages and game flow improvements
- Added play-again functionality

## License 📄

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Future Enhancements 💡

Potential next steps could include:
- AI opponent (single-player mode)
- Game statistics tracking
- Different difficulty levels
- Network multiplayer
- GUI version
- Save/load game states
