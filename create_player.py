from Player import Player

def create_player():
    print('Welcome to Los Santos!  The city where you can be anyone you want.  A criminal, a cop, a racer, a hacker, a civilian.  You decide!')
    player_1_name = input("What is your name? ").title()

    player_1_driving_ability = input("How well can you drive a car? Type: bad, good, or great: ").lower()
    while player_1_driving_ability != 'bad' and player_1_driving_ability != "good" and player_1_driving_ability != 'great':
        player_1_driving_ability = input('Tony says you are dumb and can\'t type.  Enter bad, good, or great as your driving ablility: ').lower()

    player_1_hacking_ability = input('Have you hacked a laptop before?  Would you say you are a beginner, average or expert hackerman? ').lower()
    while player_1_hacking_ability != 'beginner' and player_1_hacking_ability != 'average' and player_1_hacking_ability != 'expert':
        player_1_hacking_ability = input('Yuno thinks you may have accidentally typed something wrong.  Please type either beginner, average, or expert for your hacking ability: ').lower()

    player_1 = Player(player_1_name, player_1_driving_ability, player_1_hacking_ability, 5000)
    print(player_1)
    return player_1