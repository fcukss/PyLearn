"""
our task is to create a function that does four
basic mathematical operations.

The function should take three arguments
- operation(string/char), value1(number), value2(number).
The function should return result of numbers
after applying the chosen operation.
"""


def basic_op(operator, num1, num2):
    if num2==0:
        return 0
    else:
        return {'+': num1 + num2,
                '-': num1 - num2,
                '*': num1 * num2,
                '/': num1 / num2}[operator]


print(basic_op('+',4,7))
print(basic_op('*',15,18))



def repeat_str(repeat, string):
    return 'string'*repeat

print(repeat_str(4,"st"))

def litres(time):

    return time % 0.5

print(litres(3))
print(3.5)