from Board import Board
from Computer import Computer
from Player import Player
import sys

b = Board()
comp_1 = Computer(b,'X')
player_2 = Player(b,'Player 2','O')

count_moves = 1 #count total moves played
while count_moves<((b.ROWS+1)*(b.COLS+1)):    
    
    comp_1.move()      
    if b.has_winner() == True:
        print('Computer wins :(')
        sys.exit(0)   
    
    count_moves += 1
    
    player_2.user_move()  
    if b.has_winner() == True:
        print('Player 2 wins!')
        sys.exit(0)
    count_moves += 1
    
    input("Press Enter to continue")
    


print("Wow you tied. Good game.")

