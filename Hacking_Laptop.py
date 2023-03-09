import random

class Hacking_Laptop:
    def __init__(self, color, price, attempts_left, locations, pay_out):
        self.color = color
        self.price = price
        self.attempts_left = attempts_left
        self.locations = locations
        self.pay_out = pay_out
        self.success_rates = []

    def __repr__(self):
        return "This {color} hacking laptop can be used at the following locations: {locations}.  It has 3 attempts total and {attempts_left} attempts left.".format(color = self.color, locations = self.locations, attempts_left = self.attempts_left)

    def add_success_rates(self, rate_beginner, rate_average, rate_excellent):
        self.success_rates.append(rate_beginner)
        self.success_rates.append(rate_average)
        self.success_rates.append(rate_excellent)

    def choose_hack_location(self):  
        location = input('Which location would you like to rob? {locations}: '.format(locations = self.locations)).title()
        while location not in self.locations:
            location = input('Looks like you had a typo.  Re-enter bank location: ').title()

        print('You chose to rob the {location}.  Good Luck Hackerman... Human Captcha input required!'.format(location = location))

        return location
    
    def hack_bank_beginner(self):
        hacking_success_rate = self.success_rates[0]
        system_bypass = random.randint(1, 100)
        self.attempts_left -= 1
        pass_fail = ''

        if system_bypass <= hacking_success_rate:
            print('You bypassed the security system and made ${pay_out}!'.format(pay_out = self.pay_out))
            pass_fail += 'pass'
        else:
            print('You failed the hack.')
            pass_fail += 'fail'

        if pass_fail == 'fail' and self.attempts_left > 0:
            attempt_or_attempts = ''
            if self.attempts_left == 1:
                attempt_or_attempts = 'attempt'
            else:
                attempt_or_attempts = 'attempts'

            try_again = input('This laptop has {attempts_left} {attempt_or_attempts} left.  Do you want to try the hack again?  Type either Yes or No. '.format(attempts_left = self.attempts_left, attempt_or_attempts = attempt_or_attempts)).title()
            while try_again != 'Yes' and try_again != 'No':
                try_again = input('Type Yes to try the hack again or No to keep the laptop for later. ').title()
            if try_again == 'Yes':
                self.hack_bank_beginner()

        return pass_fail
    
    def hack_bank_average(self):
        hacking_success_rate = self.success_rates[1]
        system_bypass = random.randint(1, 100)
        self.attempts_left -= 1
        pass_fail = ''

        if system_bypass <= hacking_success_rate:
            print('You bypassed the security system and made ${pay_out}!'.format(pay_out = self.pay_out))
            pass_fail += 'pass'
        else:
            print('You failed the hack.')
            pass_fail += 'fail'

        if pass_fail == 'fail' and self.attempts_left > 0:
            attempt_or_attempts = ''
            if self.attempts_left == 1:
                attempt_or_attempts = 'attempt'
            else:
                attempt_or_attempts = 'attempts'

            try_again = input('This laptop has {attempts_left} {attempt_or_attempts} left.  Do you want to try the hack again?  Type either Yes or No. '.format(attempts_left = self.attempts_left, attempt_or_attempts = attempt_or_attempts)).title()
            while try_again != 'Yes' and try_again != 'No':
                try_again = input('Type Yes to try the hack again or No to keep the laptop for later. ').title()
            if try_again == 'Yes':
                self.hack_bank_average()

        return pass_fail