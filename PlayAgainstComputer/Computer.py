from random import random

class Computer:
    
    def __init__(self, board, token):
        self.b = board
        self.token = token
        
    def move(self):
        self.b.make_move(self.decide_move(),self.token)
        print('\n'*100)
        self.b.toString()
        
    def decide_move(self):
        
        if self.token=='X':
            #Check to see if X can make 4 in a row
            for col, row in enumerate(self.b.open_row):
                if self.b.space_exists_and_empty([row,col]):
                    if self.b.spaces[row][col].x_count['total'][3]>=1:
                        return col
            #Check to see if O can make 4 in a row
            for col, row in enumerate(self.b.open_row):
                if self.b.space_exists_and_empty([row,col]):
                    if self.b.spaces[row][col].o_count['total'][3]>=1:
                        return col
           
            #store potential moves
            potential_moves = []
            #track num of direction with 2 X's.
            most=0
            
            for col, row in enumerate(self.b.open_row):
                if self.b.space_exists_and_empty([row,col]):
                    total = self.b.spaces[row][col].x_count['total'][2]
                    
                    #Check that row above will not allow opponent to win
                    
                    if self.b.space_exists_and_empty([(row-1),col]):
                        o_above = self.b.spaces[row-1][col].o_count['total'][3]
                    else: o_above = 0
                    
                    #clears potential moves if there a space with more 2 in a rows
                    if total > most and o_above < 1:
                        potential_moves = []
                        most = total
                    if total == most:
                        if o_above < 1:
                                potential_moves.append([row,col])

            #Return only move with 2 in a row
            if len(potential_moves) == 1:
                return potential_moves[0][1]                
            
            # Store tracking variables for iterations of 1 X in dirrection              
            potential_moves_2 = []
            most=0
            
            for row,col in potential_moves:
                total = self.b.spaces[row][col].x_count['total'][1]
                if total > most:
                    potential_moves_2 = []
                    most = total
                if total == most:
                    potential_moves_2.append([row,col])

            #Return only move with one in a row
            if len(potential_moves_2) == 1:
                return potential_moves_2[0][1]

            #Checking open X's around the open moves.
            potential_moves_3 = []
            most = 0
            
            for move in potential_moves_2:
                row,col = move
                count = len(self.b.spaces[row][col].open_x['d'])
                count += len(self.b.spaces[row][col].open_x['a'])
                count += len(self.b.spaces[row][col].open_x['fs'])
                count += len(self.b.spaces[row][col].open_x['bs'])

                if count > most:
                    potential_moves_3 = []
                    most = count

                if count == most:
                    potential_moves_3.append([row,col])
                    

            if len(potential_moves_3) == 1:
                return potential_moves_3[0][1]

            else:
                #plays move if there is nothing good to play
                for col, row in enumerate(self.b.open_row):
                    if row != -1:
                        return col
                       
                    
                