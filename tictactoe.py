# Terminal Tic Tac Toe Game in Python
import os

# ANSI color codes for colorful output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def clear_screen():
    """Clear the terminal screen for better visibility"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    """Print the current game board with position numbers as reference"""
    print("\n" + Colors.CYAN + "="*50 + Colors.RESET)
    print(Colors.BOLD + Colors.YELLOW + "           TIC-TAC-TOE GAME" + Colors.RESET)
    print(Colors.CYAN + "="*50 + Colors.RESET)
    print(f"\n{Colors.BLUE}Position Reference:{Colors.RESET}     {Colors.BOLD}Current Board:{Colors.RESET}")
    
    # Create colored X and O for better visibility
    def colorize_player(symbol):
        if symbol == "X":
            return Colors.RED + Colors.BOLD + symbol + Colors.RESET
        elif symbol == "O":
            return Colors.GREEN + Colors.BOLD + symbol + Colors.RESET
        else:
            return symbol
    
    print("  1 | 2 | 3             ", end="")
    print(f"  {colorize_player(board[0][0])} | {colorize_player(board[0][1])} | {colorize_player(board[0][2])}")
    print("  ---------             ", end="")
    print("  ---------")
    print("  4 | 5 | 6             ", end="")
    print(f"  {colorize_player(board[1][0])} | {colorize_player(board[1][1])} | {colorize_player(board[1][2])}")
    print("  ---------             ", end="")
    print("  ---------")
    print("  7 | 8 | 9             ", end="")
    print(f"  {colorize_player(board[2][0])} | {colorize_player(board[2][1])} | {colorize_player(board[2][2])}")
    print("                        ", end="")
    print("  ---------")
    print()

def position_to_coordinates(position):
    """Convert position number (1-9) to row, col coordinates"""
    position_map = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    return position_map.get(position, (-1, -1))

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def make_move(board, row, col, player):
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def get_player_move(current_player):
    """Get and validate player move input"""
    while True:
        try:
            # Color the current player
            player_color = Colors.RED if current_player == "X" else Colors.GREEN
            print(f"{player_color}{Colors.BOLD}Player {current_player}{Colors.RESET}, choose your move!")
            position = input(f"{Colors.CYAN}Enter position number (1-9): {Colors.RESET}").strip()
            
            if not position:
                print(f"{Colors.RED}❌ Please enter a number!{Colors.RESET}")
                continue
                
            position = int(position)
            
            if position < 1 or position > 9:
                print(f"{Colors.RED}❌ Please enter a number between 1 and 9!{Colors.RESET}")
                continue
                
            return position
            
        except ValueError:
            print(f"{Colors.RED}❌ Please enter a valid number!{Colors.RESET}")
            continue

def play_game():
    """Main game loop"""
    clear_screen()
    print(f"{Colors.MAGENTA}{Colors.BOLD}🎮 Welcome to Tic-Tac-Toe! 🎮{Colors.RESET}")
    print(f"{Colors.YELLOW}Players will take turns. Player {Colors.RED}X{Colors.YELLOW} goes first.{Colors.RESET}")
    input(f"{Colors.CYAN}Press Enter to start the game...{Colors.RESET}")
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        clear_screen()
        print_board(board)
        
        # Get player move
        position = get_player_move(current_player)
        row, col = position_to_coordinates(position)
        
        # Validate and make move
        if not make_move(board, row, col, current_player):
            print(f"{Colors.RED}❌ That position is already taken! Try again.{Colors.RESET}")
            input(f"{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
            continue
            
        # Check for winner
        if check_winner(board, current_player):
            clear_screen()
            print_board(board)
            winner_color = Colors.RED if current_player == "X" else Colors.GREEN
            print(f"{Colors.YELLOW}🎉 Congratulations! Player {winner_color}{Colors.BOLD}{current_player}{Colors.RESET}{Colors.YELLOW} wins! 🎉{Colors.RESET}")
            break
            
        # Check for draw
        if is_draw(board):
            clear_screen()
            print_board(board)
            print(f"{Colors.BLUE}🤝 It's a draw! Good game!{Colors.RESET}")
            break
            
        # Switch players
        current_player = "O" if current_player == "X" else "X"
    
    # Ask if they want to play again
    print(f"\n{Colors.MAGENTA}Thanks for playing!{Colors.RESET}")
    play_again = input(f"{Colors.CYAN}Would you like to play again? (y/n): {Colors.RESET}").strip().lower()
    if play_again in ['y', 'yes']:
        play_game()
    else:
        print(f"{Colors.YELLOW}Goodbye! 👋{Colors.RESET}")

if __name__ == "__main__":
    play_game()

