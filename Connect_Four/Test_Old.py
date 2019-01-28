from BoardClass import Board
from BoardChecker import BoardChecker

b = Board()
   
bc = BoardChecker(b)

bc.board.toString()

count = 0

while True:

    token = 'X'
    bc.board.make_move(int(input('Player 1:')),token)
    bc.board.toString()
    if bc.has_winner() == True:
        print('Player 1 wins!')
        break
            
    token = 'O'
    bc.board.make_move(int(input('Player 2:')),token)
    bc.board.toString()
    if bc.has_winner() == True:
        print('Player 2 wins!')
        break