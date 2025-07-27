# Tic-Tac-Tao 🎮

A terminal-based Tic-Tac-Toe game written in Python that brings the classic strategy game to your command line.

## Features

- **Interactive Terminal Gameplay**: Clean and simple interface
- **Two-Player Mode**: Play against a friend locally
- **Input Validation**: Robust error handling for invalid moves
- **Win Detection**: Automatic detection of wins and draws
- **Multiple Games**: Play as many rounds as you want

## How to Play

1. **Start the Game**:
   ```bash
   python3 tictactoe.py
   ```

2. **Make Your Move**:
   - Enter your move as two numbers: `row column`
   - Use coordinates from 1-3 for both row and column
   - Example: `2 1` places your mark in the middle-left position

3. **Game Board Layout**:
   ```
   1,1 | 1,2 | 1,3
   ---------------
   2,1 | 2,2 | 2,3  
   ---------------
   3,1 | 3,2 | 3,3
   ```

4. **Winning**:
   - Get three of your marks (X or O) in a row
   - Rows, columns, or diagonals all count as wins
   - The game automatically detects wins and draws

## Requirements

- Python 3.x
- No additional dependencies required

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/xhon-pelushi/Tic-Tac-Tao.git
   cd Tic-Tac-Tao
   ```

2. Run the game:
   ```bash
   python3 tictactoe.py
   ```

## Example Gameplay

```
  |   |  
---------
  |   |  
---------
  |   |  
---------

Player X, enter your move (row col): 2 2

  |   |  
---------
  | X |  
---------
  |   |  
---------

Player O, enter your move (row col): 1 1

O |   |  
---------
  | X |  
---------
  |   |  
---------
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork this project and submit pull requests with improvements!