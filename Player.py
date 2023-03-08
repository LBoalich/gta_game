#create player class
class Player:
  def __init__(self, name, driving_ability, hacking_ability, money_total):
    self.name = name
    self.driving_ability = driving_ability
    self.hacking_ability = hacking_ability
    self.money_total = money_total
    self.laptops = []