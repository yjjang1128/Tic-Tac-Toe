def insert_letter(pos, letter):
    board[pos] = letter

def is_space_free(pos, letter):
    if board[pos] == ' ':
        return True

def img():
    return """
 {} | {} | {}
---|---|---
 {} | {} | {}
---|---|---
 {} | {} | {}
""".format(board[0], board[1], board[2],
           board[3], board[4], board[5],
           board[6], board[7], board[8])



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


def player1():
    run = True
    letter = 'O'
    while run:
        try:
            pos = int(input())
            if (0 <= pos) and (pos <= 8):
                if is_space_free(pos, letter):
                    insert_letter(pos, letter)
                    print(img())
                    run = False
                    return game_end(letter)
                else: 
                    print('That space has already been selected.')
            else: 
                print("Enter an integer between '0' and '8'.")
        except:
            print("Input int.")


def player2():
    run = True
    letter = 'X'
    while run:
        try:
            pos = int(input())
            if (0 <= pos) and (pos <= 8):
                if is_space_free(pos, letter):
                    insert_letter(pos, letter)
                    print(img())
                    run = False
                    return game_end(letter)
                else: 
                    print('That space has already been selected.')
            else: 
                print("Enter an integer between '0' and '8'.")
        except:
            print("Input int.")

def game_end(let):
    if win(let):
        return 'win'
    elif board.count(' ') == 0:
        return 'draw'
    else:
        return 'keep'

def draw():
    if board.count(' ') == 0:
        return True

def game_start():
    # Create board.
    global board
    board = [' ' for _ in range(9)]
    print(img())
    while True:
        ans1 = player1()
        if ans1 == 'win':
            print('player1 you win')
            break
        
        if ans1 == 'draw':
            print('draw')
            break

        ans2 = player2()
        if ans2 == 'win':
            print('player2 you win')
            break

game_start()
