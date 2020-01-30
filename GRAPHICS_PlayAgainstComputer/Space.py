'''
The Space object tracks the pieces played within four spaces on the board.
This allows the computer to determine it's opptimal defensive and offensive
moves.
'''
class Space:
    
    def __init__(self):
        self.token = ' ' #Contains token played in space: X/O
        self.index = [] #Contains spaces relation in the board
        self.open_x = {'d':[], 'a':[], 'fs':[], 'bs':[]} #Contain index of Spaces in each direction that could contribute 4 in a row for X
        self.open_o = {'d':[], 'a':[], 'fs':[], 'bs':[]} #Contain index of Spaces in each direction that could contribute 4 in a row for O
        self.has_x = {'d':[], 'a':[], 'fs':[], 'bs':[]} #Contain index of Spaces in each direction that are contributing to a potential 4 in a row for X
        self.has_o = {'d':[], 'a':[], 'fs':[], 'bs':[]} #Contain index of Spaces in each direction that are contributing to a potential 4 in a row for O
        
        #contain count with number of directions containing X/O in a row
        #used for computer to evaluate the next best move
        self.x_count = {'total':{1:0,2:0,3:0},'d':0, 'a':0, 'fs':0, 'bs':0}
        self.o_count = {'total':{1:0,2:0,3:0}, 'd':0, 'a':0, 'fs':0, 'bs':0}
        