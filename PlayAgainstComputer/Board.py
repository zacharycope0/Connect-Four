#Import space object to track spaces on Board
from Space import Space

#represents a four square board
class Board: 
    
    def __init__(self):
        #dictionary for all spaces on board
        self.spaces = [[Space() for x in list(range(8))] for x in list(range(7))]
        #highest row containing open move in each column
        self.open_row = [6]*8
        #contains the last move
        self.last_move = []
        #contains number of moves played
        self.num_moves = 0
        #set space index and open spaces next to each space
        self.setup_space_index()
        self.setup_open()
    
    #Update space.x_count & o_count so that the computer can evaluate next best move
    def update_comp_moves(self,row,col,direction):
        
        #Empty x dicts if they could not create four in a row 
        if len(self.spaces[row][col].has_x[direction]) + len(self.spaces[row][col].open_x[direction]) < 3:
            self.spaces[row][col].has_x[direction] = []
            self.spaces[row][col].open_x[direction] = []
            
        
        #Empty o dictsif they could not create four in a row    
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

    #Make a move on the board
    def make_move(self, move, token):
        if move>=0 and move<=7:
            row = self.open_row[move]
            if row >= 0:
                if token=='X':
                    self.spaces[row][move].token = ('\033[0;37;41m' + token + '\033[0m')
                else:
                    self.spaces[row][move].token = ('\033[0;37;46m' + token + '\033[0m')
                self.open_row[move] -= 1
                self.last_move = [row,move]
                self.update_space_dicts(token)
                self.num_moves += 1
        """
            else:
                print('The column that you have selected if full. Try a new move.')
        else: print('The column that you have selected if is not an eligable move. Select a column from 0-7.')
        """
    def update_space_dicts(self,token):
        row,col = self.last_move
                                
        shift = 1
        while shift < 4:
            #Update open down parameters
            if self.space_exists_and_empty([row-shift,col]):
                self.make_changes((row-shift),(col),'d',row,col,token,True)                           

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
    
    #called by update_space_dicts to make changes to the dictionaries.
    def make_changes(self,shifted_r,shifted_c,direction,row,col,token,first_check):
        if token == "X":
            if self.contains(self.spaces[shifted_r][shifted_c].open_x[direction],[row,col]):   
                self.spaces[shifted_r][shifted_c].has_x[direction].append([row,col])
            
            for r,c in reversed(self.spaces[shifted_r][shifted_c].has_o[direction]):
                    if self.to_remove_check(r,c,row,col,direction,first_check):
                        self.spaces[shifted_r][shifted_c].has_o[direction].remove([r,c])
            for r,c in reversed(self.spaces[shifted_r][shifted_c].open_o[direction]):
                    if self.to_remove_check(r,c,row,col,direction,first_check):
                        self.spaces[shifted_r][shifted_c].open_o[direction].remove([r,c])            
        
        elif token == "O":
            if self.contains(self.spaces[shifted_r][shifted_c].open_o[direction],[row,col]):   
                self.spaces[shifted_r][shifted_c].has_o[direction].append([row,col])
            
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
        
        #make changes to self.x_count&o_count
        self.update_comp_moves(shifted_r,shifted_c,direction)
    
    #check that a row and column value exist in a space_list 
    def contains(self,space_list,space):
        contains = False
        for s in space_list:
            if s == space:
                contains = True
        return contains
    
    #check whether or not the space is blocked by the new token
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
        #return whether or not to remove index
        return remove             
                          
    #check that the space exists and doesn't contain a token
    def space_exists_and_empty(self,index):
        #Check that row and columns are in bounds
        if index[0] >= 0 and index[0] <= 6 and index[1] >= 0 and index[1] <= 7:
            #Check that space doesn't contain a token
            if self.spaces[index[0]][index[1]].token == ' ':
                return True
            else: return False
        else: return False
           
    #set-up board.space.index 
    def setup_space_index(self):
        row = 6
        while row >= 0:
            col = 7            
            while col >=0:
                self.spaces[row][col].index = [row,col]
                col -= 1            
            row -=1
    
    #set-up board.space dictionaries
    def setup_open(self):
        row = 6
        while row >= 0:
            col = 7
            
            while col >=0:
                                  
                shift = 1
                while shift < 4:
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
                col -= 1            
            row -=1
            
    def check_move(self,move):
        if self.open_row[move] >= 0:
            return True
        else:
            return False
                                            
    def toString(self):
        print(" 0   1   2   3   4   5   6   7")
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.spaces[0][0].token,self.spaces[0][1].token,self.spaces[0][2].token,self.spaces[0][3].token,self.spaces[0][4].token,self.spaces[0][5].token,self.spaces[0][6].token,self.spaces[0][7].token))
        print("------------------------------")        
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.spaces[1][0].token,self.spaces[1][1].token,self.spaces[1][2].token,self.spaces[1][3].token,self.spaces[1][4].token,self.spaces[1][5].token,self.spaces[1][6].token,self.spaces[1][7].token))
        print("------------------------------")        
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.spaces[2][0].token,self.spaces[2][1].token,self.spaces[2][2].token,self.spaces[2][3].token,self.spaces[2][4].token,self.spaces[2][5].token,self.spaces[2][6].token,self.spaces[2][7].token))
        print("------------------------------")        
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.spaces[3][0].token,self.spaces[3][1].token,self.spaces[3][2].token,self.spaces[3][3].token,self.spaces[3][4].token,self.spaces[3][5].token,self.spaces[3][6].token,self.spaces[3][7].token))
        print("------------------------------")        
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.spaces[4][0].token,self.spaces[4][1].token,self.spaces[4][2].token,self.spaces[4][3].token,self.spaces[4][4].token,self.spaces[4][5].token,self.spaces[4][6].token,self.spaces[4][7].token))
        print("------------------------------")        
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.spaces[5][0].token,self.spaces[5][1].token,self.spaces[5][2].token,self.spaces[5][3].token,self.spaces[5][4].token,self.spaces[5][5].token,self.spaces[5][6].token,self.spaces[5][7].token))
        print("------------------------------")        
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.spaces[6][0].token,self.spaces[6][1].token,self.spaces[6][2].token,self.spaces[6][3].token,self.spaces[6][4].token,self.spaces[6][5].token,self.spaces[6][6].token,self.spaces[6][7].token))
    
        #Change last move from red to black
        r,c = self.last_move
        token = self.spaces[r][c].token[-5]
        
        if token == 'X':
            self.spaces[r][c].token = ('\033[31m' + token + '\033[0m')
        else:
            self.spaces[r][c].token = ('\033[36m' + token + '\033[0m')
    #to delete
    #'\033[31m'
    #
    #UPDATE CODE BELOW
    #
    def has_winner(self):
        
        winner = False
            
        while winner == False:
            row,col = self.last_move
            token = self.spaces[row][col].token
            count = 0 # keep track of num in row
            
            # check down
            down_check = [[row+3,col],[row+2, col],[row+1, col]]
            for_slash_check = [[row+3,col-3] , [row+2,col-2] , [row+1,col-1]]
            back_slash_check = [[row+3,col+3] , [row+2,col+2] , [row+1,col+1]]
            side_check = [[row,col-3] , [row,col-2] , [row,col-1]]
            
            #Check down                       
            if self.spots_have_token(down_check, token) == True:
                winner = True
                return winner
                break
            
            #Check forward-slash
            while count <= 3:                
                if self.spots_have_token(for_slash_check, token) == True:
                    winner = True
                    return winner
                    break
                else:
                    try:                   
                        row, col = for_slash_check[count]
                        for_slash_check[count] = [row-4, col+4]
                        count += 1
                    except:
                        count += 1
            
            #Check back-slash
            count = 0
            while count <= 3:                
                if self.spots_have_token(back_slash_check, token) == True:
                    winner = True
                    return winner
                    break
                else:
                    try:                  
                        row, col = back_slash_check[count]
                        back_slash_check[count] = [row-4, col-4]
                        count += 1
                    except:
                        count += 1
                    
            #Check side to side
            count = 0
            while count <= 3:                
                if self.spots_have_token(side_check, token) == True:
                    winner = True
                    return winner
                    break
                else:
                    try:                   
                        row, col = side_check[count]
                        side_check[count] = [row, col+4]
                        count += 1
                    except:
                        count += 1
                    
            #If no winner        
            return winner
            break
    
    def spots_have_token(self, spots, token):
        have_token = True
        
        for spot in spots:
            try:
                if self.spaces[spot[0]][spot[1]].token != token:
                    have_token = False
            except:
                have_token = False
        
        return have_token 
                 