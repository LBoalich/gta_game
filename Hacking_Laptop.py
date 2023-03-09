class Hacking_Laptop:
  def __init__(self, color, price, attempts_left, locations, pay_out):
    self.color = color
    self.price = price
    self.attempts_left = attempts_left
    self.locations = locations
    self.pay_out = pay_out
    self.success_rates = []

  def __repr__(self):
    return 'This {color} hacking laptop can be used at the following locations: {locations}.  It has 3 attempts total and {attempts_left} attempts left.'.format(color = self.color, can_be_used_at = self.locations, attempts_left = self.attempts_left)

