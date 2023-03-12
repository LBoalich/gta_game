from Player import Player
from create_player import create_player
from race_or_rob import race_or_rob

#create Buddha, Tony, Yuno players
lang_buddha = Player('Lang Buddha', 'bad', 'average', 5000)
tony_corleone = Player('Tony Corleone', 'great', 'beginner', 500)
yuno_sykk = Player('Yuno Sykk', 'good', 'exellent', 500)

#create new player
player_1 = create_player()
player_1_laptop_inventory = []

race_or_rob(player_1, player_1_laptop_inventory, lang_buddha, tony_corleone, yuno_sykk)
