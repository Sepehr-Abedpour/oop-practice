import random

class Human :
    def __init__(self,name) :
        self.name = name

class Football_player(Human) :
    def __init__(self,name) :
        super().__init__(name) 
        self.team = ''

names = [
    'hossein','maziar','akbar','nima','mehdi','mohammad','khashayar','milad','mostafa','amin','farhad','poya','pourya','reza','ali','behza','saeed','behrouz','shahrouz','saman','mohsen','soheil'
]
players = []
for name in names :
    player = Football_player(name)
    players.append(player)

random.shuffle(players)

for i in range (22) :
    if i < 11 :
        players[i].team = 'A'
    else :
        players[i].team = 'B'

for player in players :
    print('player_name :',player.name,'team:',player.team)
    