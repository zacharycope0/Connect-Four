from Board import Board
from Computer import Computer
from Player import Player
import pygame
import sys

b = Board()
comp_1 = Computer(b,'X')
player_2 = Player(b,'Player 2','O')

count_moves = 1 #count total moves played

pygame.init()

SQUARESIZE = 100
width = (b.COLS + 1) * SQUARESIZE
height = (b.ROWS + 2) * SQUARESIZE  

size = (width, height)

screen = pygame.display.set_mode(size)

#https://www.youtube.com/watch?v=SDz3P_Ctm7U

"""
while count_moves<(56-1):    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:


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

"""