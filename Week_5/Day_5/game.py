import random

class Game:
    def __init__(self):
        pass

    def get_user_item(self):
        self.user_item = input('select your choice\n(r)ock\n(p)aper\n(s)cissors\n')
        while self.user_item in "rR" or "pP" or "sS":
            return self.user_item
        else:
            print('not a vaid option.try again!')
            self.get_user_item()
 
    
    def get_computer_item(self):
        self.computer_item = random.choice(['r', 'p', 's'])
        return self.computer_item


    def get_game_results(self, user_item, computer_item):
        self.user_item = user_item
        self.computer_item = computer_item
        if self.computer_item == self.user_item:
            return 'draw'
        elif computer_item == 'r' and user_item == 'p':
            return 'win'
        elif computer_item == 'p' and user_item == 's':
            return 'win'
        elif computer_item == 's' and user_item == 'r':
            return 'win'
        else:
            return 'loss'

    def play(self):
        user_item = self.get_user_item
        computer_item = self.get_computer_item
        result = self.get_game_results(user_item,computer_item)
        print(f'You selected {self.user_item}. The computer selected {self.computer_item}. You {result}!')
        return result

            
game = Game()  
game.play()


