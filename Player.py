class Player:
    def __init__(self, name, driving_ability, hacking_ability, money_total):
        self.name = name
        self.driving_ability = driving_ability
        self.hacking_ability = hacking_ability
        self.money_total = money_total
        self.laptops = []

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
    
    def buy_laptop(self):
        laptop_list = [['green', 100], ['blue', 300], ['black', 500], ['red', 1000], ['gold', 5000]]
        laptop_string = 'The laptop prices are: '
        laptop_color_string = ''
        laptop_color_list = []

        for laptop in laptop_list:
            if laptop[0] in self.laptops:
                pass
            else:
                laptop_string += ('{laptop_color} ${laptop_price}, '.format(laptop_color = laptop[0], laptop_price = str(laptop[1])))
                laptop_color_string += (laptop[0] + ' ')
                laptop_color_list.append(laptop[0])

        print('You have ${amount}.'.format(amount = self.money_total))
        print(laptop_string)

        laptop_color = input('Which color laptop do you want to buy? ').lower()
        
        while laptop_color not in laptop_color_list:
            laptop_color = input('Looks like you had a typo.  Please re-enter the color laptop you want to purchase: ').lower()

        for laptops in laptop_list:
            if laptop_color == laptops[0]:
                laptop_price = laptops[1]

        if self.money_total < laptop_price:
            print("You do not have enough money to buy that laptop.  Sadge.  Pick a different laptop sucker!")
            self.buy_laptop()
        else:
            self.money_total -= laptop_price
            self.laptops.append(laptop_color)
            print('You spent ${laptop_price} and now have ${money_total} left.'.format(laptop_price = laptop_price, money_total = self.money_total))
            return laptop_color
