from race import race
from rob import rob

def race_or_rob(player_1, player_1_laptop_inventory, lang_buddha, tony_corleone, yuno_sykk):
    player_list = ['Lang Buddha', 'Tony Corleone', 'Yuno Sykk']
    choose_race_or_rob = input('Los Santos is an exciting place to live.  Do you want to challenge someone to a race or rob a bank?  Enter: race or rob: ').lower()
    while choose_race_or_rob != 'race' and choose_race_or_rob != 'rob':
        choose_race_or_rob = input("Mr. Budhha says you are a sucker you can\'t type!  Enter race or rob: ").lower()

    if choose_race_or_rob == 'race':
        opponent = input('You chose to race!  Put on some music with the good vibes and pick an opponent.  You can race Lang Buddha, Tony Corleone, or Yuno Sykk.  Pick the player you want to race: ').title()
        while opponent not in player_list:
            opponent = input('WWWW..WWWaaa..Wake up Samurai!  Enter: Lang Buddha, Tony Corleone, or Yuno Sykk: ').title()

        if opponent == "Lang Buddha":
            player_2 = lang_buddha
        elif opponent == "Tony Corleone":
            player_2 = tony_corleone
        else:
            player_2 = yuno_sykk

        has_money = race(player_1, player_2)
        if has_money == True:
            race_or_rob(player_1, player_1_laptop_inventory, lang_buddha, tony_corleone, yuno_sykk)

    elif choose_race_or_rob == 'rob':
        #check for players laptops and buy if none
        if player_1.laptops == [] and player_1.money_total < 100:
            print('You don\'t have any laptops and don\'t have enough money to buy one.  You better go racing instead.')
            race_or_rob(player_1, player_1_laptop_inventory, lang_buddha, tony_corleone, yuno_sykk)
        else:
            continue_game = rob(player_1, player_1_laptop_inventory)
            if continue_game == True:
                race_or_rob(player_1, player_1_laptop_inventory, lang_buddha, tony_corleone, yuno_sykk)
