import random
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                      (0, 4, 8), (2, 4, 6)]         
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False
def check_draw(board):
    return all(space != ' ' for space in board)


def available_moves(board):
    return [i for i, space in enumerate(board) if space == ' ']

def computer_move(board):
    move = random.choice(available_moves(board))
    board[move] = 'O'


def tic_tac_toe():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        try:
            user_move = int(input("Enter your move (1-9): ")) - 1
            if board[user_move] != ' ':
                print("Invalid move, spot already taken!")
                continue
        except (ValueError, IndexError):
            print("Please enter a valid move (1-9).")
            continue
        
        board[user_move] = 'X'
        print_board(board)
        
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        
        if check_draw(board):
            print("It's a draw!")
            break
        
       
        print("Computer's turn...")
        computer_move(board)
        print_board(board)
        
        if check_winner(board, 'O'):
            print("Sorry, the computer wins!")
            break
        
        if check_draw(board):
            print("It's a draw!")
            break

tic_tac_toe()
