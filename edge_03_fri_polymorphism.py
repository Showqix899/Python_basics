#defingin a Player Class

class Player:

    def play(self):
        pass


#creating a Football player class

class FootballPlayer(Player):

    def __init__(self,name):
        self.name = name

    def play(self):
        print(f'{self.name} is playing Football ')


#creating a cricket player class
class CricketPlayer(Player):

    def __init__(self,name):
        self.name = name

    def play(self):
        print(f'{self.name} is playing Cricket ')


#creating object of FootballPlayer calss
football_player=FootballPlayer('messi')
#creating object for CricketPlayer class
cricket_player=CricketPlayer('smith')


#showing the informatin
football_player.play()
cricket_player.play()