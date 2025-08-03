#!/usr/bin/env python3
"""
Tic Tac Toe GUI Game using Tkinter
A simple graphical version of the classic game
"""

import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x500")
        self.window.resizable(False, False)
        
        # Game state
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.buttons = []
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.window, 
            text="Tic Tac Toe", 
            font=("Arial", 24, "bold"),
            fg="blue"
        )
        title_label.pack(pady=10)
        
        # Current player display
        self.status_label = tk.Label(
            self.window,
            text=f"Player {self.current_player}'s turn",
            font=("Arial", 16),
            fg="green"
        )
        self.status_label.pack(pady=5)
        
        # Game board frame
        board_frame = tk.Frame(self.window)
        board_frame.pack(pady=20)
        
        # Create 3x3 grid of buttons
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(
                    board_frame,
                    text=" ",
                    font=("Arial", 20, "bold"),
                    width=4,
                    height=2,
                    command=lambda r=row, c=col: self.make_move(r, c),
                    bg="lightgray",
                    relief="raised",
                    bd=2
                )
                button.grid(row=row, column=col, padx=2, pady=2)
                button_row.append(button)
            self.buttons.append(button_row)
        
        # Control buttons frame
        control_frame = tk.Frame(self.window)
        control_frame.pack(pady=20)
        
        # New game button
        new_game_btn = tk.Button(
            control_frame,
            text="New Game",
            font=("Arial", 14),
            command=self.new_game,
            bg="lightblue",
            padx=20
        )
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        # Quit button
        quit_btn = tk.Button(
            control_frame,
            text="Quit",
            font=("Arial", 14),
            command=self.window.quit,
            bg="lightcoral",
            padx=20
        )
        quit_btn.pack(side=tk.LEFT, padx=10)
        
    def make_move(self, row, col):
        if self.game_over or self.board[row][col] != " ":
            return
            
        # Make the move
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(
            text=self.current_player,
            fg="red" if self.current_player == "X" else "blue",
            state="disabled"
        )
        
        # Check for win or draw
        if self.check_winner(self.current_player):
            self.game_over = True
            self.status_label.config(
                text=f"Player {self.current_player} wins! 🎉",
                fg="purple"
            )
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.disable_all_buttons()
        elif self.is_draw():
            self.game_over = True
            self.status_label.config(text="It's a draw! 🤝", fg="orange")
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            # Switch players
            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(
                text=f"Player {self.current_player}'s turn",
                fg="green"
            )
    
    def check_winner(self, player):
        # Check rows
        for row in range(3):
            if all(self.board[row][col] == player for col in range(3)):
                return True
        
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            return True
            
        return False
    
    def is_draw(self):
        return all(self.board[row][col] != " " for row in range(3) for col in range(3))
    
    def disable_all_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state="disabled")
    
    def new_game(self):
        # Reset game state
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.game_over = False
        
        # Reset UI
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(
                    text=" ",
                    state="normal",
                    bg="lightgray"
                )
        
        self.status_label.config(
            text=f"Player {self.current_player}'s turn",
            fg="green"
        )
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
