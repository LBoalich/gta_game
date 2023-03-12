import sys
from Hacking_Laptop import Hacking_Laptop

#pick laptop color to rob bank
def rob(player_1, player_1_laptop_inventory):
    global player_1_green
    global player_1_blue
    global player_1_red
    global player_1_gold
    global player_1_black
    new_laptop_color = ''

    #use laptop you already own or buy new one.  Add to laptop inventory list.
    if len(player_1.laptops) == 0:
        new_laptop_color = player_1.buy_laptop()
    else:
        color_list = ', '.join(player_1.laptops)
        new_laptop = input('You have the following laptops: {player_1_laptops}.  You can use one of these laptops or buy a new one.  Type \'yes\' to buy a new one or \'no\' to use one you already own: '.format(player_1_laptops = color_list)).lower()

        while new_laptop != 'yes' and new_laptop != 'no':
            new_laptop = input('You have the following laptops: {player_1_laptops}.  You can use one of these laptops or buy a new one.  Type \'yes\' to buy a new one or \'no\' to use one you already own: '.format(player_1_laptops = color_list)).lower()

        if new_laptop == 'yes':
            new_laptop_color = player_1.buy_laptop()

    if new_laptop_color != '':
        if new_laptop_color == 'green':
            player_1_green = Hacking_Laptop('green', 100, 3, "Fleeca Bank, Bay City Bank", 200)
            player_1_green.add_success_rates(40, 90, 95)
            player_1_laptop_inventory.append(player_1_green)
        elif new_laptop_color == "blue":
            player_1_blue = Hacking_Laptop('blue', 300, 3, "Paleto Bank, Pink Cage Bank", 500)
            player_1_blue.add_success_rates(20, 75, 90)
            player_1_laptop_inventory.append(player_1_blue)
        elif new_laptop_color == 'red':
            player_1_red = Hacking_Laptop('red', 1000, 3, "the Upper Vault", 4000)
            player_1_red.add_success_rates(10, 30, 85)
            player_1_laptop_inventory.append(player_1_red)
        elif new_laptop_color == 'gold':
            player_1_gold = Hacking_Laptop('gold', 5000, 3, "the Lower Vault", 9000)
            player_1_gold.add_success_rates(5, 15, 75)
            player_1_laptop_inventory.append(player_1_gold)
        elif new_laptop_color == 'black':
            player_1_black = Hacking_Laptop('black', 500, 3, "the Yacht", 5000)
            player_1_black.add_success_rates(2, 5, 60)  
            player_1_laptop_inventory.append(player_1_black)

    #chose laptop color to use and hack based on player hacking ability.  Add payout to player_1 money total.  Remove used laptop from laptop inventory list and player_1.laptops

    color_list = (', '.join(player_1.laptops))
    laptop_color_choice = input('You have the following laptops: {player_1_laptops}.  Which color laptop do you want to use? '.format(player_1_laptops = color_list)).lower()
    while laptop_color_choice not in player_1.laptops:
        laptop_color_choice = input('Yuno says you have to pick a laptop that is in your inventory or you had a typo.  Please re-enter: ').lower()

    pass_fail = ''

    #green
    if laptop_color_choice == 'green':
        player_1_green.choose_hack_location()

        if player_1.hacking_ability == 'beginner':
            pass_fail = player_1_green.hack_bank_beginner()
        elif player_1.hacking_ability == 'average':
            pass_fail = player_1_green.hack_bank_average()
        elif player_1.hacking_ability == 'expert':
            pass_fail = player_1_green.hack_bank_expert()

        if pass_fail == 'pass':
            player_1.money_total += player_1_green.pay_out
            player_1.laptops.remove('green')
            print('This laptop is all used up and has been removed from your inventory.')

        elif pass_fail == 'fail':
            if player_1_green.attempts_left == 0:
                player_1_laptop_inventory.remove(player_1_green)
                player_1.laptops.remove('green')
                print('This laptop is all used up and has been removed from your inventory.')

            if player_1.money_total <= 0 and len(player_1.laptops) == 0:
                print('You do not have any money left and you have no laptops in your inventory.  Sadge.  GAME OVER')
                sys.exit()

    #blue
    elif laptop_color_choice == 'blue':
        player_1_blue.choose_hack_location()

        if player_1.hacking_ability == 'beginner':
            pass_fail = player_1_blue.hack_bank_beginner()
        elif player_1.hacking_ability == 'average':
            pass_fail = player_1_blue.hack_bank_average()
        elif player_1.hacking_ability == 'expert':
            pass_fail = player_1_blue.hack_bank_expert()

        if pass_fail == 'pass':
            player_1.money_total += player_1_blue.pay_out
            player_1.laptops.remove('blue')
            print('This laptop is all used up and has been removed from your inventory.')

        elif pass_fail == 'fail':
            if player_1_blue.attempts_left == 0:
                player_1_laptop_inventory.remove(player_1_blue)
                player_1.laptops.remove('blue')
                print('This laptop is all used up and has been removed from your inventory.')

            if player_1.money_total <= 0 and len(player_1.laptops) == 0:
                print('You do not have any money left and you have no laptops in your inventory.  Sadge.  GAME OVER')
                sys.exit()

    #red
    elif laptop_color_choice == 'red':
        player_1_red.choose_hack_location()

        if player_1.hacking_ability == 'beginner':
            pass_fail = player_1_red.hack_bank_beginner()
        elif player_1.hacking_ability == 'average':
            pass_fail = player_1_red.hack_bank_average()
        elif player_1.hacking_ability == 'expert':
            pass_fail = player_1_red.hack_bank_expert()

        if pass_fail == 'pass':
            player_1.money_total += player_1_red.pay_out
            player_1.laptops.remove('red')
            print('This laptop is all used up and has been removed from your inventory.')

        elif pass_fail == 'fail':
            if player_1_red.attempts_left == 0:
                player_1_laptop_inventory.remove(player_1_red)
                player_1.laptops.remove('red')
                print('This laptop is all used up and has been removed from your inventory.')

            if player_1.money_total <= 0 and len(player_1.laptops) == 0:
                print('You do not have any money left and you have no laptops in your inventory.  Sadge.  GAME OVER')
                sys.exit()

    #gold
    elif laptop_color_choice == 'gold':
        player_1_gold.choose_hack_location()

        if player_1.hacking_ability == 'beginner':
            pass_fail = player_1_gold.hack_bank_beginner()
        elif player_1.hacking_ability == 'average':
            pass_fail = player_1_gold.hack_bank_average()
        elif player_1.hacking_ability == 'expert':
            pass_fail = player_1_gold.hack_bank_expert()

        if pass_fail == 'pass':
            player_1.money_total += player_1_gold.pay_out
            player_1.laptops.remove('gold')
            print('This laptop is all used up and has been removed from your inventory.')

        elif pass_fail == 'fail':
            if player_1_gold.attempts_left == 0:
                player_1_laptop_inventory.remove(player_1_gold)
                player_1.laptops.remove('gold')
                print('This laptop is all used up and has been removed from your inventory.')

            if player_1.money_total <= 0 and len(player_1.laptops) == 0:
                print('You do not have any money left and you have no laptops in your inventory.  Sadge.  GAME OVER')
                sys.exit()

    #black
    elif laptop_color_choice == 'black':
        player_1_black.choose_hack_location()

        if player_1.hacking_ability == 'beginner':
            pass_fail = player_1_black.hack_bank_beginner()
        elif player_1.hacking_ability == 'average':
            pass_fail = player_1_black.hack_bank_average()
        elif player_1.hacking_ability == 'expert':
            pass_fail = player_1_black.hack_bank_expert()

        if pass_fail == 'pass':
            player_1.money_total += player_1_black.pay_out
            player_1.laptops.remove('black')
            print('This laptop is all used up and has been removed from your inventory.')

        elif pass_fail == 'fail':
            if player_1_black.attempts_left == 0:
                player_1_laptop_inventory.remove(player_1_black)
                player_1.laptops.remove('black')
                print('This laptop is all used up and has been removed from your inventory.')

            if player_1.money_total <= 0 and len(player_1.laptops) == 0:
                print('You do not have any money left and you have no laptops in your inventory.  Sadge.  GAME OVER')
                sys.exit()

    return True
