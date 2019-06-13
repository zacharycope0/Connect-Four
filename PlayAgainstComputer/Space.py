class Space:
    
    def __init__(self):
        self.token = ' '
        self.index = []
        self.open_x = {'d':[], 'a':[], 'fs':[], 'bs':[]}
        self.open_o = {'d':[], 'a':[], 'fs':[], 'bs':[]}
        self.has_x = {'d':[], 'a':[], 'fs':[], 'bs':[]}
        self.has_o = {'d':[], 'a':[], 'fs':[], 'bs':[]}
        #contain count with number of dirrections containing X/O in a row
        self.x_count = {'total':{1:0,2:0,3:0},'d':0, 'a':0, 'fs':0, 'bs':0}
        self.o_count = {'total':{1:0,2:0,3:0}, 'd':0, 'a':0, 'fs':0, 'bs':0}
        