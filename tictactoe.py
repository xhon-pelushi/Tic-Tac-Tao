# Terminal Tic Tac Toe Game in Python

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Example usage:
board = [[" " for _ in range(3)] for _ in range(3)]
print_board(board)

