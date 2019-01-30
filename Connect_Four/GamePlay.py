#hold functions for game play
class GamePlay:
    
    def __init__(self,board_checker):
        self.bc = board_checker

    def user_move(self, player, token):    
        while True:
            try:
                input_move = int(input('{} 1:'.format(player)))
                while self.bc.board.check_move(input_move) != True:
                    input_move = int(input('No space in column. Try again:'))
                break
            except:
                print("Value out of range try again")

        self.bc.board.make_move(input_move,token)
        self.bc.board.toString()
        if self.bc.has_winner() == True:
            print('{} wins!'.format(player))
            return True
        else:
            return False

