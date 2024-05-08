#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_board(board):
    """
    Prints the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """
    Checks if there is a winner.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None

def is_board_full(board):
    """
    Checks if the board is full.
    """
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def print_scorecard(score):
    """
    Prints the current scorecard.
    """
    print("\nSCORECARD")
    print("---------")
    print(f"Player X: {score['X']} wins")
    print(f"Player O: {score['O']} wins")
    print(f"Ties: {score['T']}")

def main():
    """
    Main function to run the Tic-Tac-Toe game.
    """
    score = {'X': 0, 'O': 0, 'T': 0}
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'
        print("\nWelcome to Tic-Tac-Toe!\n")
        print("Instructions:")
        print("Enter the row and column numbers to place your mark.")
        print("Row and column numbers should be between 0 and 2.\n")
        print("Let's begin!\n")
        while True:
            print_board(board)
            row = input(f"Player {current_player}, enter row (0, 1, or 2): ")
            col = input(f"Player {current_player}, enter column (0, 1, or 2): ")

            # Validate input
            if not row.isdigit() or not col.isdigit():
                print("Invalid input! Please enter numbers only.")
                continue
            row, col = int(row), int(col)
            if not (0 <= row <= 2) or not (0 <= col <= 2):
                print("Row and column numbers should be between 0 and 2.")
                continue

            if board[row][col] != ' ':
                print("That cell is already occupied. Try again.")
                continue
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"\nPlayer {winner} wins!")
                score[winner] += 1
                break
            if is_board_full(board):
                print_board(board)
                print("\nIt's a tie!")
                score['T'] += 1
                break
            current_player = 'O' if current_player == 'X' else 'X'
        
        print_scorecard(score)
        replay = input("\nDo you want to play again? (yes/no): ")
        if replay.lower() != 'yes':
            print("\nThank you for playing!")
            break

if __name__ == "__main__":
    main()


# In[ ]:




