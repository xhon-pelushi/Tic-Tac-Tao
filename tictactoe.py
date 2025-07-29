# Terminal Tic Tac Toe Game in Python
import os
import random
import time
import threading
import signal
import sys

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

# AI Functions
def get_available_positions(board):
    """Get all available positions on the board"""
    available = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                # Convert row, col to position number (1-9)
                position = row * 3 + col + 1
                available.append(position)
    return available

def ai_easy_move(board):
    """Easy AI: Makes random moves"""
    available_positions = get_available_positions(board)
    if available_positions:
        return random.choice(available_positions)
    return None

def ai_medium_move(board, ai_player):
    """Medium AI: Blocks player wins and tries to win"""
    available_positions = get_available_positions(board)
    
    # First, try to win
    for position in available_positions:
        row, col = position_to_coordinates(position)
        # Test if this move wins
        board[row][col] = ai_player
        if check_winner(board, ai_player):
            board[row][col] = " "  # Undo test move
            return position
        board[row][col] = " "  # Undo test move
    
    # Second, block opponent from winning
    opponent = "X" if ai_player == "O" else "O"
    for position in available_positions:
        row, col = position_to_coordinates(position)
        # Test if opponent would win with this move
        board[row][col] = opponent
        if check_winner(board, opponent):
            board[row][col] = " "  # Undo test move
            return position
        board[row][col] = " "  # Undo test move
    
    # Otherwise, make a random move
    return random.choice(available_positions) if available_positions else None

def ai_hard_move(board, ai_player):
    """Hard AI: Uses minimax algorithm for optimal play"""
    def minimax(board, depth, is_maximizing, ai_player, human_player):
        # Check terminal states
        if check_winner(board, ai_player):
            return 10 - depth
        if check_winner(board, human_player):
            return depth - 10
        if is_draw(board):
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = ai_player
                        score = minimax(board, depth + 1, False, ai_player, human_player)
                        board[row][col] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = human_player
                        score = minimax(board, depth + 1, True, ai_player, human_player)
                        board[row][col] = " "
                        best_score = min(score, best_score)
            return best_score
    
    best_position = None
    best_score = float('-inf')
    human_player = "X" if ai_player == "O" else "O"
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = ai_player
                score = minimax(board, 0, False, ai_player, human_player)
                board[row][col] = " "
                
                if score > best_score:
                    best_score = score
                    best_position = row * 3 + col + 1
    
    return best_position

def get_ai_move(board, ai_player, difficulty):
    """Get AI move based on difficulty level"""
    print(f"{Colors.YELLOW}🤖 AI is thinking...{Colors.RESET}")
    time.sleep(1)  # Add thinking delay for better UX
    
    if difficulty == "easy":
        return ai_easy_move(board)
    elif difficulty == "medium":
        return ai_medium_move(board, ai_player)
    elif difficulty == "hard":
        return ai_hard_move(board, ai_player)
    else:
        return ai_easy_move(board)  # Default to easy

def get_game_mode():
    """Get game mode selection from user"""
    clear_screen()
    print(f"{Colors.MAGENTA}{Colors.BOLD}🎮 TIC-TAC-TOE GAME MODES 🎮{Colors.RESET}")
    print(f"{Colors.CYAN}="*50 + Colors.RESET)
    print(f"\n{Colors.YELLOW}Choose your game mode:{Colors.RESET}")
    print(f"{Colors.BLUE}1.{Colors.RESET} Two Players (Human vs Human)")
    print(f"{Colors.BLUE}2.{Colors.RESET} Single Player vs AI")
    print(f"{Colors.BLUE}3.{Colors.RESET} Time Attack Mode (Human vs AI with time limit)")
    print()
    
    while True:
        try:
            choice = input(f"{Colors.CYAN}Enter your choice (1, 2, or 3): {Colors.RESET}").strip()
            if choice == "1":
                return "human_vs_human"
            elif choice == "2":
                return "human_vs_ai"
            elif choice == "3":
                return "time_attack"
            else:
                print(f"{Colors.RED}❌ Please enter 1, 2, or 3!{Colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Goodbye! 👋{Colors.RESET}")
            exit()

def get_ai_difficulty():
    """Get AI difficulty selection from user"""
    print(f"\n{Colors.YELLOW}Choose AI difficulty:{Colors.RESET}")
    print(f"{Colors.GREEN}1.{Colors.RESET} Easy (Random moves)")
    print(f"{Colors.YELLOW}2.{Colors.RESET} Medium (Smart blocking)")
    print(f"{Colors.RED}3.{Colors.RESET} Hard (Unbeatable)")
    print()
    
    while True:
        try:
            choice = input(f"{Colors.CYAN}Enter difficulty (1, 2, or 3): {Colors.RESET}").strip()
            if choice == "1":
                return "easy"
            elif choice == "2":
                return "medium"
            elif choice == "3":
                return "hard"
            else:
                print(f"{Colors.RED}❌ Please enter 1, 2, or 3!{Colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Goodbye! 👋{Colors.RESET}")
            exit()

def get_time_limit():
    """Get time limit selection from user"""
    print(f"\n{Colors.YELLOW}Choose time limit per move:{Colors.RESET}")
    print(f"{Colors.GREEN}1.{Colors.RESET} 5 seconds (Lightning fast)")
    print(f"{Colors.YELLOW}2.{Colors.RESET} 10 seconds (Quick thinking)")
    print(f"{Colors.BLUE}3.{Colors.RESET} 15 seconds (Standard)")
    print(f"{Colors.MAGENTA}4.{Colors.RESET} 30 seconds (Relaxed)")
    print()
    
    while True:
        try:
            choice = input(f"{Colors.CYAN}Enter choice (1, 2, 3, or 4): {Colors.RESET}").strip()
            if choice == "1":
                return 5
            elif choice == "2":
                return 10
            elif choice == "3":
                return 15
            elif choice == "4":
                return 30
            else:
                print(f"{Colors.RED}❌ Please enter 1, 2, 3, or 4!{Colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Goodbye! 👋{Colors.RESET}")
            exit()

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

class TimedInput:
    def __init__(self, timeout):
        self.timeout = timeout
        self.user_input = None
        self.timeout_occurred = False
    
    def get_input(self, prompt):
        """Get input with timeout"""
        self.user_input = None
        self.timeout_occurred = False
        
        # Start countdown display in separate thread
        countdown_thread = threading.Thread(target=self._countdown_display)
        countdown_thread.daemon = True
        countdown_thread.start()
        
        # Get user input
        try:
            self.user_input = input(prompt)
        except (EOFError, KeyboardInterrupt):
            self.timeout_occurred = True
            return None
            
        return self.user_input if not self.timeout_occurred else None
    
    def _countdown_display(self):
        """Display countdown timer"""
        for remaining in range(self.timeout, 0, -1):
            if self.user_input is not None:
                return
            
            # Display countdown
            color = Colors.RED if remaining <= 3 else Colors.YELLOW if remaining <= 5 else Colors.GREEN
            print(f"\r{color}⏰ Time remaining: {remaining} seconds{Colors.RESET}", end="", flush=True)
            time.sleep(1)
        
        if self.user_input is None:
            self.timeout_occurred = True
            print(f"\r{Colors.RED}⏰ TIME'S UP! Making random move...{Colors.RESET}")

def get_timed_player_move(current_player, time_limit, board):
    """Get player move with time limit"""
    while True:
        try:
            player_color = Colors.RED if current_player == "X" else Colors.GREEN
            print(f"\n{player_color}{Colors.BOLD}Player {current_player}{Colors.RESET}, choose your move!")
            
            timed_input = TimedInput(time_limit)
            position_str = timed_input.get_input(f"{Colors.CYAN}Enter position number (1-9): {Colors.RESET}")
            
            if timed_input.timeout_occurred or position_str is None:
                # Time's up! Make random move
                available_positions = get_available_positions(board)
                if available_positions:
                    position = random.choice(available_positions)
                    print(f"{Colors.RED}⏰ Random move selected: {position}{Colors.RESET}")
                    time.sleep(1)
                    return position
                return None
            
            position_str = position_str.strip()
            if not position_str:
                print(f"{Colors.RED}❌ Please enter a number!{Colors.RESET}")
                continue
                
            position = int(position_str)
            
            if position < 1 or position > 9:
                print(f"{Colors.RED}❌ Please enter a number between 1 and 9!{Colors.RESET}")
                continue
                
            return position
            
        except ValueError:
            print(f"{Colors.RED}❌ Please enter a valid number!{Colors.RESET}")
            continue
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Game interrupted! 👋{Colors.RESET}")
            sys.exit()

def play_game():
    """Main game loop with mode selection"""
    # Get game mode
    game_mode = get_game_mode()
    
    # Setup game variables
    ai_difficulty = None
    ai_player = None
    time_limit = None
    
    if game_mode in ["human_vs_ai", "time_attack"]:
        ai_difficulty = get_ai_difficulty()
        ai_player = "O"  # AI always plays as O
        
        if game_mode == "time_attack":
            time_limit = get_time_limit()
            clear_screen()
            print(f"{Colors.MAGENTA}{Colors.BOLD}⚡ TIME ATTACK MODE ⚡{Colors.RESET}")
            print(f"{Colors.YELLOW}AI Difficulty: {ai_difficulty.title()}{Colors.RESET}")
            print(f"{Colors.CYAN}Time Limit: {time_limit} seconds per move{Colors.RESET}")
            print(f"{Colors.YELLOW}You are {Colors.RED}X{Colors.YELLOW}, AI is {Colors.GREEN}O{Colors.YELLOW}. You go first!{Colors.RESET}")
            print(f"{Colors.RED}⚠️  If you don't move in time, a random move will be made!{Colors.RESET}")
        else:
            clear_screen()
            print(f"{Colors.MAGENTA}{Colors.BOLD}🎮 Human vs AI ({ai_difficulty.title()}) 🎮{Colors.RESET}")
            print(f"{Colors.YELLOW}You are {Colors.RED}X{Colors.YELLOW}, AI is {Colors.GREEN}O{Colors.YELLOW}. You go first!{Colors.RESET}")
    else:
        clear_screen()
        print(f"{Colors.MAGENTA}{Colors.BOLD}🎮 Human vs Human 🎮{Colors.RESET}")
        print(f"{Colors.YELLOW}Player {Colors.RED}X{Colors.YELLOW} goes first.{Colors.RESET}")
    
    input(f"{Colors.CYAN}Press Enter to start the game...{Colors.RESET}")
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        clear_screen()
        print_board(board)
        
        # Get move based on current player and game mode
        if game_mode in ["human_vs_ai", "time_attack"] and current_player == ai_player:
            # AI move
            position = get_ai_move(board, ai_player, ai_difficulty)
            if position is None:
                break  # Should not happen, but safety check
            print(f"{Colors.YELLOW}🤖 AI chooses position {position}!{Colors.RESET}")
            time.sleep(1.5)  # Show AI choice briefly
        else:
            # Human move
            if game_mode == "time_attack":
                position = get_timed_player_move("You", time_limit, board)
            elif game_mode == "human_vs_ai":
                position = get_player_move("You")
            else:
                position = get_player_move(current_player)
        
        if position is None:
            continue
            
        row, col = position_to_coordinates(position)
        
        # Validate and make move
        if not make_move(board, row, col, current_player):
            if game_mode in ["human_vs_ai", "time_attack"] and current_player != ai_player:
                print(f"{Colors.RED}❌ That position is already taken! Try again.{Colors.RESET}")
                input(f"{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
            elif game_mode == "human_vs_human":
                print(f"{Colors.RED}❌ That position is already taken! Try again.{Colors.RESET}")
                input(f"{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
            continue
            
        # Check for winner
        if check_winner(board, current_player):
            clear_screen()
            print_board(board)
            winner_color = Colors.RED if current_player == "X" else Colors.GREEN
            
            if game_mode in ["human_vs_ai", "time_attack"]:
                if current_player == ai_player:
                    if game_mode == "time_attack":
                        print(f"{Colors.RED}🤖 AI wins the Time Attack! Better luck next time! ⚡{Colors.RESET}")
                    else:
                        print(f"{Colors.RED}🤖 AI wins! Better luck next time! 🤖{Colors.RESET}")
                else:
                    if game_mode == "time_attack":
                        print(f"{Colors.YELLOW}🎉 Amazing! You beat the AI in Time Attack mode! ⚡🎉{Colors.RESET}")
                    else:
                        print(f"{Colors.YELLOW}🎉 Congratulations! You beat the AI! 🎉{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}🎉 Congratulations! Player {winner_color}{Colors.BOLD}{current_player}{Colors.RESET}{Colors.YELLOW} wins! 🎉{Colors.RESET}")
            break
            
        # Check for draw
        if is_draw(board):
            clear_screen()
            print_board(board)
            if game_mode in ["human_vs_ai", "time_attack"]:
                if game_mode == "time_attack":
                    print(f"{Colors.BLUE}🤝 Time Attack Draw! You held your ground against the AI! ⚡{Colors.RESET}")
                else:
                    print(f"{Colors.BLUE}🤝 It's a draw! You played well against the AI!{Colors.RESET}")
            else:
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

