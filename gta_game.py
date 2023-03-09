from Player import Player
from Hacking_Laptop import Hacking_Laptop

#create Buddha, Tony, Yuno
lang_buddha = Player('Lang Buddha', 'bad', 'average', 5000)
tony_corleone = Player('Tony Corleone', 'great', 'beginner', 500)
yuno_sykk = Player('Yuno Sykk', 'good', 'exellent', 500)

#create hacking laptops
green_laptop = Hacking_Laptop('green', 100, 3, "Fleeca Bank, Bay City Bank", 200)
green_laptop.add_success_rates(40, 90, 95)
blue_laptop = Hacking_Laptop('blue', 300, 3, "Paleto Bank, Pink Cage Bank", 500)
blue_laptop.add_success_rates(20, 75, 90)
red_laptop = Hacking_Laptop('red', 1000, 3, "the Upper Vault", 4000)
red_laptop.add_success_rates(10, 30, 85)
gold_laptop = Hacking_Laptop('gold', 5000, 3, "the Lower Vault", 9000)
gold_laptop.add_success_rates(5, 15, 75)
black_laptop = Hacking_Laptop('black', 500, 3, "the Yacht", 5000)
black_laptop.add_success_rates(2, 5, 60)

