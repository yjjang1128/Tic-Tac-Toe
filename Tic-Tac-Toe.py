def insert_letter(pos, letter):
    board[pos] = letter

def player1():
    pos = int(input())
    letter = "O"
    insert_letter(pos, letter)
    print(board)
    if win(letter) == True:
        return True
    else:
        return False

def player2():
    pos = int(input())
    letter = "X"
    insert_letter(pos, letter)
    print(board)
    if win(letter) == True:
        return True
    else:
        return False

# If win, return True
def win(let):
    return (
        # Set row.
        (board[0] == board[1] == board[2] == let) or
        (board[3] == board[4] == board[5] == let) or
        (board[6] == board[7] == board[8] == let) or
        # Set column. 
        (board[0] == board[3] == board[6] == let) or
        (board[1] == board[4] == board[7] == let) or
        (board[2] == board[5] == board[8] == let) or
        # Set diagonal.
        (board[0] == board[4] == board[8] == let) or
        (board[2] == board[4] == board[6] == let)
        )

def draw():
    if board.count(" ") == 0:
        return True

def game_start():
    global board
    board = [' ' for _ in range(9)]
    game_end = False

    while True:
        if game_end == True:
            break
        else:
            game_end = player1()
        
        if game_end == True:
            break
        else:   
            game_end = player2()

game_start()
