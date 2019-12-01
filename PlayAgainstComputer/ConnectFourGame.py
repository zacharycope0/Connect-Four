from Board import Board
from Computer import Computer
from Player import Player

b = Board()
comp_1 = Computer(b,'X')
player_2 = Player(b,'Player 2','O')

b.make_move(3,'X')
b.toString()

count_moves = 1 #count total moves played
game_over = False
while count_moves<(56-1):    
    
    player_2.user_move()  
    if b.has_winner() == True:
        print('Player 2 wins!')
        break
    
    input("Press Enter to continue")
    
    comp_1.move()      
    if b.has_winner() == True:
        print('Computer wins :(')
        break
    
    

    count_moves += 2

