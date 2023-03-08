#create player class
class Player:
    def __init__(self, name, driving_ability, hacking_ability, money_total):
        self.name = name
        self.driving_ability = driving_ability
        self.hacking_ability = hacking_ability
        self.money_total = money_total
        self.laptops = []

    #player description
    def __repr__(self):
        a_an = ''
        current_laptops = ''

        if self.hacking_ability == 'beginner':
            a_an = 'a'
        else:
            a_an = 'an'

        if self.laptops == []:
            current_laptops = 'None'
        else:
            current_laptops = ', '.join(self.laptops)

        return "My name is {name}.  I am {a_or_an} {hacking_ability} level hacker.  I am {driving_ability} at driving a car.  I have ${money_total} and am currently carrying the following laptops: {laptops}.".format(name = self.name, hacking_ability = self.hacking_ability, driving_ability = self.driving_ability, a_or_an = a_an, money_total = self.money_total, laptops = current_laptops)

