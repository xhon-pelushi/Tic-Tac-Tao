# Tic-Tac-Tao ⚡🎮

A colorful, feature-rich terminal-based Tic-Tac-Toe game written in Python with AI opponents and exciting game modes!

## Features ✨

### Game Modes 🎯
- **Human vs Human** - Classic two-player mode
- **Human vs AI** - Challenge the computer with 3 difficulty levels
- **⚡ Time Attack Mode** - Race against the clock with time-limited moves!

### AI Difficulty Levels 🤖
- **Easy** - Random moves (perfect for beginners)
- **Medium** - Smart blocking and basic strategy
- **Hard** - Unbeatable AI using Minimax algorithm

### ⚡ NEW: Time Attack Features
- **Multiple time limits**: 5, 10, 15, or 30 seconds per move
- **Visual countdown timer** with color-coded warnings
- **Auto-random moves** when time runs out
- **Enhanced pressure** for competitive gameplay

### Enhanced User Experience
- **Clear visual layout** with numbered grid positions (1-9) for easy input
- **Colorful interface** with ANSI color codes:
  - Player X appears in **red**
  - Player O appears in **green**
  - AI moves highlighted in **yellow**
  - Time warnings in **red/yellow/green**
- **Screen clearing** between moves for a clean gaming experience
- **Improved input validation** with helpful error messages
- **Position reference guide** displayed alongside the current board
- **Play again option** after each game

### Game Features
- Win condition detection (rows, columns, diagonals)
- Draw condition detection
- Input validation and error handling
- Turn-based gameplay with clear player indicators
- Real-time countdown timers (Time Attack mode)

## How to Play 🎯

1. Run the game: `python tictactoe.py`
2. Choose your game mode:
   - **Mode 1**: Human vs Human
   - **Mode 2**: Human vs AI (choose difficulty)
   - **Mode 3**: ⚡ Time Attack - Human vs AI with time limits!
3. In Time Attack mode, select your time limit (5-30 seconds per move)
4. Players take turns choosing positions 1-9:
   ```
   Position Reference:
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```
5. **⚡ Time Attack**: Make your move before the countdown reaches zero!
6. Player X goes first (displayed in red)
7. AI/Player O goes second (displayed in green)
8. First player to get three in a row wins!
9. Choose to play again or exit after each game

## Requirements 📋

- Python 3.x
- Terminal with ANSI color support (most modern terminals)

## Installation & Running 🚀

```bash
# Clone the repository
git clone https://github.com/xhon-pelushi/Tic-Tac-Tao.git

# Navigate to the directory
cd Tic-Tac-Tao

# Run the game
python tictactoe.py
```

## Recent Updates 🆕

### Version 2.0 - Time Attack Mode! ⚡
- **NEW**: Time Attack mode with customizable time limits
- **NEW**: Real-time countdown timers with visual feedback
- **NEW**: Auto-random moves when time expires
- **Enhanced**: Better game mode selection
- **Enhanced**: Improved user interface and messaging

### Version 1.0 - AI & Enhanced Features 🤖
- Added AI opponent with 3 difficulty levels
- Implemented Minimax algorithm for unbeatable Hard mode
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
- Game statistics and score tracking
- Sound effects and animations  
- Different board sizes (4x4, 5x5)
- Network multiplayer
- GUI version using tkinter or pygame
- Save/load game states
- Tournament mode
- Hint system for players
- AI personality traits

## Contributing 🤝

Feel free to fork this project and submit pull requests for any improvements!

## Screenshots 📸

```
🎮 TIC-TAC-TOE GAME MODES 🎮
==================================================

Choose your game mode:
1. Two Players (Human vs Human)
2. Single Player vs AI  
3. Time Attack Mode (Human vs AI with time limit) ⚡

⚡ TIME ATTACK MODE ⚡
AI Difficulty: Hard
Time Limit: 10 seconds per move
⚠️  If you don't move in time, a random move will be made!

⏰ Time remaining: 7 seconds
```
