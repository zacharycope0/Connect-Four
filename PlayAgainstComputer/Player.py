#hold functions for game play
class Player:
    
    def __init__(self,board,player,token):
        self.b = board
        self.player = player
        self.token = token

    def user_move(self):    
        while True:
            try:
                input_move = int(input('{} input move:'.format(self.player)))
                while self.b.check_move(input_move) != True:
                    input_move = int(input('No space in column. Try again:'))
                break
            except:
                print("Value out of range try again")

        self.b.make_move(input_move,self.token)
        print('\n'*100)
        self.b.toString()
        

