from typing import Union
from functools import reduce

class Modulo11Calculator:
    def get_factor(self, num):
        digits = [2, 3, 4, 5, 6, 7, 8, 9]
        if num >= len(digits):
            index = num % len(digits)
        else:
            index = num
        return digits[index]
    
    def compute_reversed_digits(self, num):
        num = str(num)
        digits = [int(digit) for digit in num]
        digits.reverse()
        return digits
    
    def compute_factors(self, reversed_digits):
        return [self.get_factor(i) for i in range(0, len(reversed_digits))]

    def compute_sum(self, reversed_digits, factors):
        return reduce(lambda prev, data: prev + (data[0] * data[1]), zip(reversed_digits, factors), 0)

    def compute_verify_digit(self, sum):
        value = 11 - (sum % 11)
        if value >= 10:
            return 0
        return value

    def __call__(self, num: Union[int, str]) -> int:
        digits = self.compute_reversed_digits(num)
        factors = self.compute_factors(digits)
        sum = self.compute_sum(digits, factors)
        return self.compute_verify_digit(sum)

compute_check_digit = Modulo11Calculator()
