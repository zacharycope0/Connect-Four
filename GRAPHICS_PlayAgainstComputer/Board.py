'''
The Board object creates a connect four board with Space objects. It updates necessary Space objects
after each move
'''
#Import space object to track spaces on Board
from Space import Space
import numpy as np

#represents a connect four board
class Board: 
    
    def __init__(self):
        #set columns and rows in board
        self.ROWS = 7 
        self.COLS = 8 
        #create 2D list for all spaces on board
        self.spaces = [[Space() for x in list(range(self.COLS))] for x in list(range(self.ROWS))]
        #highest row containing open move in each column. Set to start at bottom row
        self.array = np.zeros((self.ROWS,self.COLS))
        self.open_row = [6]*8                               
        #contains the last move played
        self.last_move = []
        #tracks number of moves played
        self.num_moves = 0
        #Set Space.index to track the postion of each space on the board
        self.setup_space_index()
        #Set Space.open_x and Space.open_o to track open spaces withing 4 potions on the board
        self.setup_open()

    
#****************************************************************************************************
#BOARD SET-UP: Updating space objects
#****************************************************************************************************  

    #set-up Space.index for each space in board
    def setup_space_index(self):
        for row in range(self.ROWS): #stops iterations after rows 0-6 have been updated        
            for col in range(self.COLS): #stops iterations after cols 0-7 have been updated
                self.spaces[row][col].index = [row,col] #sets index
    
    #set-up  Space.open_x and Space.open_o for each space in board
    def setup_open(self):
        for row in range(self.ROWS): #stops iterations after rows 0-6 have been updated        
            for col in range(self.COLS): #stops iterations after cols 0-7 have been updated
                                  
                shift = 1 #reprents distance between spaces on board (1 would be a space dirrectly next to the space being updated)
                while shift <= 3: #stops iteration when shift is greater than 3
                    #Update open down parameters
                    if self.space_exists_and_empty([row+shift,col]):
                        self.spaces[row+shift][col].open_x['d'].append([row,col])
                        self.spaces[row+shift][col].open_o['d'].append([row,col])
                    if self.space_exists_and_empty([row-shift,col]):
                        self.spaces[row-shift][col].open_x['d'].append([row,col])
                        self.spaces[row-shift][col].open_o['d'].append([row,col])
                                    
                    #update open forward-slash
                    if self.space_exists_and_empty([row+shift,col-shift]):
                        self.spaces[row+shift][col-shift].open_x['fs'].append([row,col])
                        self.spaces[row+shift][col-shift].open_o['fs'].append([row,col])
                    if self.space_exists_and_empty([row-shift,col+shift]):
                        self.spaces[row-shift][col+shift].open_x['fs'].append([row,col])
                        self.spaces[row-shift][col+shift].open_o['fs'].append([row,col])
                    
                    #update open back-slash
                    if self.space_exists_and_empty([row-shift,col-shift]):
                        self.spaces[row-shift][col-shift].open_x['bs'].append([row,col])
                        self.spaces[row-shift][col-shift].open_o['bs'].append([row,col])
                    if self.space_exists_and_empty([row+shift,col+shift]):
                        self.spaces[row+shift][col+shift].open_x['bs'].append([row,col])
                        self.spaces[row+shift][col+shift].open_o['bs'].append([row,col])
                    
                    #update open accross
                    if self.space_exists_and_empty([row,col-shift]):
                        self.spaces[row][col-shift].open_x['a'].append([row,col])
                        self.spaces[row][col-shift].open_o['a'].append([row,col])
                    if self.space_exists_and_empty([row,col+shift]):
                        self.spaces[row][col+shift].open_x['a'].append([row,col])
                        self.spaces[row][col+shift].open_o['a'].append([row,col])
                    shift += 1                       
    
#****************************************************************************************************
#GAME PLAY UPDATES: Updates Space objects after a move is made
#****************************************************************************************************

    #Make a move on the board and updates Space object attributes around move
    def make_move(self, move, token):
        row = self.open_row[move] #determine the row index of the move
           
        self.spaces[row][move].token = token #update space with token
        self.open_row[move] -= 1 #update open row attribute
        self.last_move = [row,move] #update last_move attribute
        self.update_space_dicts(token) #update space attributes
        self.num_moves += 1

    #updates the Space dictionary attributes
    def update_space_dicts(self,token):
        row,col = self.last_move
                                
        shift = 1 #track distance around token played
        while shift <= 3: #only update Space dicts within 3 spaces of the last move
            #Update open down parameters
            if self.space_exists_and_empty([row-shift,col]): #Check that space exists
                self.make_changes((row-shift),(col),'d',row,col,token,True) #Make changes if space exists                           

            #update open forward-slash
            if self.space_exists_and_empty([row+shift,col-shift]):
                self.make_changes((row+shift),(col-shift),'fs',row,col,token,True)                
            if self.space_exists_and_empty([row-shift,col+shift]):
                self.make_changes((row-shift),(col+shift),'fs',row,col,token,False)
                
            
            #update open back-slash
            if self.space_exists_and_empty([row-shift,col-shift]):
                self.make_changes((row-shift),(col-shift),'bs',row,col,token,True)                 
            if self.space_exists_and_empty([row+shift,col+shift]):
                self.make_changes((row+shift),(col+shift),'bs',row,col,token,False)

            
            #update open accross
            if self.space_exists_and_empty([row,col-shift]):
                self.make_changes(row,(col-shift),'a',row,col,token,True)
            if self.space_exists_and_empty([row,col+shift]):
                self.make_changes(row,(col+shift),'a',row,col,token,False)
            shift += 1
    
    #Makes changes to the Space dictionaries that track moves in the area.
    #Called by update_space_dicts 
    def make_changes(self,shifted_r,shifted_c,direction,row,col,token,first_check):
        if token == "X":
            if self.contains(self.spaces[shifted_r][shifted_c].open_x[direction],[row,col]): #check that move/[row,col] exists in Space.open_x   
                self.spaces[shifted_r][shifted_c].has_x[direction].append([row,col]) #append move to Space.has_x 
            
            #Updates Space.has_o and Space.open_o to account for X blocking the O's in a given direction
            for r,c in reversed(self.spaces[shifted_r][shifted_c].has_o[direction]): 
                    if self.to_remove_check(r,c,row,col,direction,first_check): 
                        self.spaces[shifted_r][shifted_c].has_o[direction].remove([r,c])
            for r,c in reversed(self.spaces[shifted_r][shifted_c].open_o[direction]):
                    if self.to_remove_check(r,c,row,col,direction,first_check):
                        self.spaces[shifted_r][shifted_c].open_o[direction].remove([r,c])            
        
        elif token == "O":
            if self.contains(self.spaces[shifted_r][shifted_c].open_o[direction],[row,col]): #check that move/[row,col] exists in Space.open_o  
                self.spaces[shifted_r][shifted_c].has_o[direction].append([row,col]) #append move to Space.has_o
            
            #Updates Space.has_x and Space.open_x to account for O blocking the X's in a given direction
            for r,c in reversed(self.spaces[shifted_r][shifted_c].has_x[direction]):
                    if self.to_remove_check(r,c,row,col,direction,first_check):
                        self.spaces[shifted_r][shifted_c].has_x[direction].remove([r,c])
            for r,c in reversed(self.spaces[shifted_r][shifted_c].open_x[direction]):
                    if self.to_remove_check(r,c,row,col,direction,first_check):
                        self.spaces[shifted_r][shifted_c].open_x[direction].remove([r,c])
        
        try:
            self.spaces[shifted_r][shifted_c].open_x[direction].remove([row,col])
        except:
            pass
        try:    
            self.spaces[shifted_r][shifted_c].open_o[direction].remove([row,col])
        except:
            pass
        
        #Update Space.x_count and Space.o_count
        self.update_comp_moves(shifted_r,shifted_c,direction)

    #Update space.x_count & o_count so that the computer can evaluate next best move
    def update_comp_moves(self,row,col,direction):
        
        #Empty x dicts if they could not create four in a row in given direction
        if len(self.spaces[row][col].has_x[direction]) + len(self.spaces[row][col].open_x[direction]) < 3:
            self.spaces[row][col].has_x[direction] = []
            self.spaces[row][col].open_x[direction] = []
            
        
        #Empty o dictsif they could not create four in a row in given direction    
        if len(self.spaces[row][col].has_o[direction]) + len(self.spaces[row][col].open_o[direction]) < 3:
            self.spaces[row][col].has_o[direction] = []
            self.spaces[row][col].open_o[direction] = [] 
        
        #Update x_count and o_count        
        #Setup parameters to count max x's and o's in a row.        
        index_to_offset = 0
        in_a_row_x = 0
        in_a_row_o = 0
        #Setup lists of values in a row
        down_check = [[row+3,col],[row+2, col],[row+1, col]]
        for_slash_check = [[row+3,col-3] , [row+2,col-2] , [row+1,col-1]]
        back_slash_check = [[row+3,col+3] , [row+2,col+2] , [row+1,col+1]]
        across_check = [[row,col-3] , [row,col-2] , [row,col-1]]
        
        while index_to_offset <= 3: 
            #down
            if direction == 'd':
                in_a_row_x = self.count_duplicates(self.spaces[row][col].has_x['d'], down_check)
                in_a_row_o = self.count_duplicates(self.spaces[row][col].has_o['d'], down_check)
            #break out of loop
                index_to_offset += 4
                
            #forwardslash     
            elif direction == 'fs':
                # update in_a_row_x
                x = self.count_duplicates(self.spaces[row][col].has_x['fs'], for_slash_check)
                if in_a_row_x < x: in_a_row_x = x
                # update in_a_row_o
                o = self.count_duplicates(self.spaces[row][col].has_o['fs'], for_slash_check)
                if in_a_row_o < o: in_a_row_o = o 
                
                #offset list and add 1 to index_to_offset           
                if index_to_offset < 3:
                    r, c = for_slash_check[index_to_offset]
                    for_slash_check[index_to_offset] = [r-4, c+4]                
                index_to_offset += 1
            
            #backslash
            elif direction == 'bs':
                # update in_a_row_x
                x = self.count_duplicates(self.spaces[row][col].has_x['bs'], back_slash_check)
                if in_a_row_x < x: in_a_row_x = x
                # update in_a_row_o
                o = self.count_duplicates(self.spaces[row][col].has_o['bs'], back_slash_check)
                if in_a_row_o < o: in_a_row_o = o 
                
                #offset list and add 1 to index_to_offset           
                if index_to_offset < 3:
                    r, c = back_slash_check[index_to_offset]
                    back_slash_check[index_to_offset] = [r-4, c-4]
                index_to_offset += 1            
            
            #accross
            else:
                # update in_a_row_x
                x = self.count_duplicates(self.spaces[row][col].has_x['a'], across_check)
                if in_a_row_x < x: in_a_row_x = x
                # update in_a_row_o
                o = self.count_duplicates(self.spaces[row][col].has_o['a'], across_check)
                if in_a_row_o < o: in_a_row_o = o 
                
                #offset list and add 1 to index_to_offset           
                if index_to_offset < 3:
                    r, c = across_check[index_to_offset]
                    across_check[index_to_offset] = [r, c+4]                    
                index_to_offset += 1
        
        #Update x_count: direction and total        
        if self.spaces[row][col].x_count[direction]>=1:
            self.spaces[row][col].x_count['total'][self.spaces[row][col].x_count[direction]] -= 1
        
        self.spaces[row][col].x_count[direction] = in_a_row_x        
        if self.spaces[row][col].x_count[direction]>=1:
            self.spaces[row][col].x_count['total'][self.spaces[row][col].x_count[direction]] += 1
        
        #Update o_count: direction and total 
        if self.spaces[row][col].o_count[direction]>=1:
            self.spaces[row][col].o_count['total'][self.spaces[row][col].o_count[direction]] -= 1
            
        self.spaces[row][col].o_count[direction] = in_a_row_o
        if self.spaces[row][col].o_count[direction]>=1:
            self.spaces[row][col].o_count['total'][self.spaces[row][col].o_count[direction]] += 1            
    
    #count duplicates between two list for update_comp_moves
    def count_duplicates(self,has_xo,check_list):
        count = 0
        for space in has_xo:
            if space in check_list:
                count += 1
        return count

    #
    #UPDATE has_winner
    #

    #Checks last move to determine if there was a winner
    def has_winner(self):
        winner = False

        row, col = self.last_move
        token = self.spaces[row][col].token

        if token == 'X':
            if self.spaces[row][col].x_count['total'][3]>0:
                winner = True
        if token == 'O':
            if self.spaces[row][col].o_count['total'][3]>0:
                winner = True

        return winner

          
              
#****************************************************************************************************
#CHECKS: Functions to check assumptions of function calls
#****************************************************************************************************

    #Check that the space exists and doesn't contain a token
    def space_exists_and_empty(self,index):
        #Check that row and columns are in bounds
        if index[0] >= 0 and index[0] <= (self.ROWS-1) and index[1] >= 0 and index[1] <= (self.COLS-1):
            #Check that space doesn't contain a token
            if self.spaces[index[0]][index[1]].token == ' ':
                return True
            else: return False
        else: return False

    #Check that a [row, col] value exist in a Space.open_x or Space.open_o
    def contains(self,space_list,space):
        contains = False
        for s in space_list:
            if s == space:
                contains = True
        return contains
           
            
    def check_move(self,move):
        if self.open_row[move] >= 0:
            return True
        else:
            return False

    #check whether the Space is blocked in a given direction by the new token
    def to_remove_check(self,r,c,row,col,direction,first_check):
        remove = False
        if direction == 'd':
            if r>row:
                remove = True
        elif direction == 'fs':
            if first_check==True:
                if r<row and c>col:
                    remove = True
            else:
                if r>row and c<col:
                    remove = True
        elif direction == 'bs':
            if first_check==True:
                if r>row and c>col:
                    remove = True
            else:
                if r<row and c<col:
                    remove = True 
        elif direction == 'a':
            if first_check==True:
                if c>col:
                    remove = True
            else:
                if c<col:
                    remove = True
        #return whether to remove index
        return remove 
    
    #****************************************************************************************************
    #DISPLAY: Functions to display the board
    #****************************************************************************************************


    #
    #
    #UPDATE: entire board to np.Array and store as Board object
    #
    #
    #Convert board to a np.array
    def toArray(self):
        # Convert last move 'X' and 'O' to 1 and 2 in array
        row, col = self.last_move
        
        if self.spaces[row][col].token == 'X':
            token = 1
        else: token =2

        self.array[row][col] = token
        
        return self.array
        
        board_array = np.zeros((self.ROWS,self.COLS))

        # # Convert 'X' and 'O' to 1 and 2 in array
        # for row in (range(self.ROWS)):
        #     for col in (range(self.COLS)):
        #         if self.spaces[row][col].token == 'X':
        #             token = 1
        #         elif self.spaces[row][col].token == 'O': 
        #             token = 2
        #         else: token = 0

        #         board_array[row][col] = token
        
        # return board_array


    #Prints board and with tokens                                        
    def toString(self):
        print("  0   1   2   3   4   5   6   7")

        for row in range(self.ROWS): #stops iterations after rows 0-6 have been updated        
            for col in range(self.COLS): #stops iterations after cols 0-7 have been updated
                print(f'| {self.spaces[row][col].token} ', end='')
            print('|\n'+'-'*33)

    
                 