#represents a four square board
class Board:
    
    def __init__(self):
        #list with all board spaces
        self.b_list = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        #highest row containing move in each column
        self.used_row_in_col = [7,7,7,7,7,7,7,7]
        #contains the last move
        self.last_move = ()
    
    def check_move(self,move):
        if self.used_row_in_col[move] != 0:
            return True
        else:
            return False
            
    def make_move(self, move, token):
        row = 6
        while row >= 0:
            if self.b_list[row][move] == ' ':
                self.b_list[row][move] = token
                self.used_row_in_col[move] = row
                self.last_move = [row,move]
                break
            else:
                row -= 1
                                            
    def toString(self):
        print(" 0   1   2   3   4   5   6   7")
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.b_list[0][0],self.b_list[0][1],self.b_list[0][2],self.b_list[0][3],self.b_list[0][4],self.b_list[0][5],self.b_list[0][6],self.b_list[0][7]))
        print("------------------------------")        
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.b_list[1][0],self.b_list[1][1],self.b_list[1][2],self.b_list[1][3],self.b_list[1][4],self.b_list[1][5],self.b_list[1][6],self.b_list[1][7]))
        print("------------------------------")        
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.b_list[2][0],self.b_list[2][1],self.b_list[2][2],self.b_list[2][3],self.b_list[2][4],self.b_list[2][5],self.b_list[2][6],self.b_list[2][7]))
        print("------------------------------")        
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.b_list[3][0],self.b_list[3][1],self.b_list[3][2],self.b_list[3][3],self.b_list[3][4],self.b_list[3][5],self.b_list[3][6],self.b_list[3][7]))
        print("------------------------------")        
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.b_list[4][0],self.b_list[4][1],self.b_list[4][2],self.b_list[4][3],self.b_list[4][4],self.b_list[4][5],self.b_list[4][6],self.b_list[4][7]))
        print("------------------------------")        
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.b_list[5][0],self.b_list[5][1],self.b_list[5][2],self.b_list[5][3],self.b_list[5][4],self.b_list[5][5],self.b_list[5][6],self.b_list[5][7]))
        print("------------------------------")        
        print(" {} | {} | {} | {} | {} | {} | {} | {}".format(self.b_list[6][0],self.b_list[6][1],self.b_list[6][2],self.b_list[6][3],self.b_list[6][4],self.b_list[6][5],self.b_list[6][6],self.b_list[6][7]))
    
    