from Board import Board
from BoardChecker import BoardChecker
from GamePlay import GamePlay

b = Board()   
bc = BoardChecker(b)
gp = GamePlay(bc)
bc.board.toString()

count_moves = 0 #count total moves played

while count_moves<56:

    if gp.user_move('Player 1', 'X') == True:
        break
    if gp.user_move('Player 2', 'O') == True:
        break
    count_moves += 2
