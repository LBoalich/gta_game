import random
import sys

def race(player_1, player_2):
  win_lose = ''
  bet = int(input('You challenged {player_2_name} to a race!  How much money do you want to bet?  You have ${money_total}: '.format(player_2_name = player_2.name, money_total = player_1.money_total)))
  while bet > player_1.money_total:
    bet = int(input('You dumb motha sucka, you can not bet more money than you have!  You have ${money_total}.  How much do you wan\'t to bet? '.format(money_total = player_1.money_total)))

  print("Let\'s get this show on the road!  Good luck {player_1_name}!!!.  3...2...1...GO!".format(player_1_name = player_1.name))
  random_int = random.randint(1, 100)

#both racers same ability
  if player_1.driving_ability == player_2.driving_ability:
    if random_int <= 50:
      player_1.money_total += bet
      win_lose = 'win'
    else:
      player_1.money_total -= bet
      win_lose = 'lose'

#player_1 one step below player_2
  elif (player_1.driving_ability == 'bad' and player_2.driving_ability == "good") or (player_1.driving_ability == 'good' and player_2.driving_ability == 'great'):
    if random_int <= 40:
      player_1.money_total += bet
      win_lose = 'win'
    else:
      player_1.money_total -= bet
      win_lose = 'lose'

#player_1 one step above player_2
  elif (player_1.driving_ability == 'good' and player_2.driving_ability == "bad") or (player_1.driving_ability == 'great' and player_2.driving_ability == 'good'):
    if random_int <= 60:
      player_1.money_total += bet
      win_lose = 'win'
    else:
      player_1.money_total -= bet
      win_lose = 'lose'

#player_1 two steps below player_2
  elif (player_1.driving_ability == 'bad' and player_2.driving_ability == "great"):
    if random_int <= 25:
      player_1.money_total += bet
      win_lose = 'win'
    else:
      player_1.money_total -= bet
      win_lose = 'lose'

#player_1 two steps above player_2
  elif (player_1.driving_ability == 'great' and player_2.driving_ability == "bad"):
    if random_int <= 75:
      player_1.money_total += bet
      
    else:
      player_1.money_total -= bet
      
#print win/lose statement
  if win_lose == 'win':
    print('Congratulations!  You won the race and made ${bet}.'.format(bet = bet))
  else:
    print("You wrecked into a local and totaled your car.  You hand over ${bet} to {player_2_name}.  Now you have ${money_total} left.".format(bet = bet, player_2_name = player_2.name, money_total = player_1.money_total))
    if player_1.money_total <= 0 and len(player_1.laptops) == 0:
      print('You do not have any money left.  Sadge.  GAME OVER')
      sys.exit()