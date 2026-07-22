import random
class Die:
    def __init__(self):
        self.side=6
        self.current_value=1

    def roll(self):
        self.current_value = random.randint(1,self.side)
        return self.current_value
    
class Player:
    def __init__(self,name):
        self.score=0
        self.name=name

    def take_turn(self,game_die):
        self.score +=game_die.roll()
        return self.score
    
game_die = Die()
player = Player("Piyush")
print(player.take_turn(game_die))
#print(game_die.roll())