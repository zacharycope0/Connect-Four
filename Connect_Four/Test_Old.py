from Board import Board
from BoardChecker import BoardChecker

b = Board()   
bc = BoardChecker(b)
bc.board.toString()

count_moves = 0 #count total moves played

while count_moves<56:

    while True:
        try:
            input_move = int(input('Player 1:'))
            while bc.board.check_move(input_move) != True:
                input_move = int(input('No space in column. Try again:'))
            break
        except:
            print("Value out of range try again")

    token = 'X'
    bc.board.make_move(input_move,token)
    count_moves += 1
    bc.board.toString()
    if bc.has_winner() == True:
        print('Player 1 wins!')
        break

    while True:
        try:
            input_move = int(input('Player 2:'))
            while bc.board.check_move(input_move) != True:
                input_move = int(input('No space in column. Try again:'))
            break
        except:
            print("Value out of range try again")

                    
    token = 'O'
    bc.board.make_move(input_move,token)
    count_moves += 1
    bc.board.toString()
    if bc.has_winner() == True:
        print('Player 2 wins!')
        break