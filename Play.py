from Board import Board
from Computer import Computer
import pygame
import sys
import math

BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)

def draw_board():
    for r in range(b.ROWS):
        for c in range(b.COLS):
            pygame.draw.rect(screen, BLUE, [c*SQUARESIZE, (r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE])
            if b.array[r][c] == 0:
                pygame.draw.circle(screen, BLACK, [int((c*SQUARESIZE) + RADIUS), int(((r+1)*SQUARESIZE) + RADIUS)], int(RADIUS-5))
            elif b.array[r][c] == 1:
                pygame.draw.circle(screen, RED, [int((c*SQUARESIZE) + RADIUS), int(((r+1)*SQUARESIZE) + RADIUS)], int(RADIUS-5)) 
            else:
                pygame.draw.circle(screen, YELLOW, [int((c*SQUARESIZE) + RADIUS), int(((r+1)*SQUARESIZE) + RADIUS)], int(RADIUS-5)) 
b = Board()
comp_1 = Computer(b,'X')

count_moves = 1 #count total moves played

pygame.init()

SQUARESIZE = 100 #pixels per square
RADIUS = SQUARESIZE/2
width = (b.COLS) * SQUARESIZE #width in pixels
height = (b.ROWS + 1) * SQUARESIZE  #high in pixels

size = (width, height) #size is tuple of moves

screen = pygame.display.set_mode(size)
draw_board()
pygame.display.update()

game_over = False
MAX_MOVES = b.COLS * b.ROWS
move_count = 0

while not game_over and move_count < MAX_MOVES:

    for event in pygame.event.get():
        
        if move_count % 2 == 0:
            #Computer move
            comp_1.move()
            print(b.toArray())
            draw_board()
            pygame.display.update()
            move_count += 1      
        
        if b.has_winner() == True:
            print('Computer wins :(')
            game_over = True
            break

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            posx = event.pos[0]
            if move_count % 2 != 0:
                pygame.draw.rect(screen, BLACK, [0, 0, width, SQUARESIZE])
                pygame.draw.circle(screen, YELLOW, [posx, int(RADIUS)], int(RADIUS-5))
                pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:

            #Ask for Player 1 input
            token = 'O'
            posx = event.pos[0]
            col = int(math.floor(posx/SQUARESIZE))
            
            b.make_move(col, token)
            move_count += 1
            print(b.toArray())
            draw_board()
            pygame.display.update()
            if b.has_winner() == True:
                print('Player 2 wins!')
                game_over = True
                break

while game_over:
    draw_board()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
            
    
