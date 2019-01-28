class BoardChecker:
    
    def __init__(self,board):
        self.board = board
        
    def spots_have_token(self, spots,marker):
        have_marker = True
        
        for spot in spots:
            try:
                if self.board.b_list[spot[0]][spot[1]] != marker:
                    have_marker = False
            except:
                have_marker = False
        
        return have_marker          
        
    def has_winner(self):
        
        winner = False
            
        while winner == False:
            row,col = self.board.last_move
            token = self.board.b_list[row][col]
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
                    


                   