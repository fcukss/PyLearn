"""
A Narcissistic Number (or Armstrong Number) is a positive number which
is the sum of its own digits, each raised to the power of the number of digits in a given base.
 In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcissistic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
"""
from itertools import count


def narcissistic( value ):
    stepen = len(str(value))
    res = 0
    for digit in str(value):
        res += int(digit)**stepen
    if res==value:
        return True
    else:
        return False

#var2
def narcissistic_2(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))


print(narcissistic(7))

def better_than_average(class_points, your_points):
    return your_points > sum(item for item in class_points)/len(class_points)

print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))