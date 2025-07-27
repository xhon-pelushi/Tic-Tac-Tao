# Terminal Tic Tac Toe Game in Python

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def print_instructions():
    print("\n" + "="*50)
    print("           Welcome to Tic-Tac-Tao!")
    print("="*50)
    print("How to play:")
    print("• Enter your move as: row column (e.g., '2 1')")
    print("• Use numbers 1-3 for both row and column")
    print("• Board positions:")
    print("  1,1 | 1,2 | 1,3")
    print("  ---------------")
    print("  2,1 | 2,2 | 2,3")
    print("  ---------------") 
    print("  3,1 | 3,2 | 3,3")
    print("="*50)

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

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print_instructions()
    
    while True:
        print_board(board)
        try:
            move = input(f"Player {current_player}, enter your move (row col): ").split()
            if len(move) != 2:
                print("Invalid input. Please enter exactly two numbers (e.g., '2 1').")
                continue
            # Convert from 1-based to 0-based indexing
            row, col = int(move[0]) - 1, int(move[1]) - 1
            
            # Validate range (now checking 1-3 input converts to 0-2)
            if not (0 <= row < 3 and 0 <= col < 3):
                print("Invalid position. Please use numbers 1-3 for row and column.")
                continue
                
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers (e.g., '2 1').")
            continue
            
        if not make_move(board, row, col, current_player):
            print("Invalid move. That position is already taken. Try again.")
            continue
            
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break
            
        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw! Good game!")
            break
            
        current_player = "O" if current_player == "X" else "X"

def main():
    """Main function to handle multiple games"""
    while True:
        play_game()
        
        while True:
            play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
            if play_again in ['y', 'yes']:
                break
            elif play_again in ['n', 'no']:
                print("Thanks for playing Tic-Tac-Tao! Goodbye! 👋")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()

