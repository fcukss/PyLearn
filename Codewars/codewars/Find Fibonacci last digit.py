#Example: getLastDigit(15) - 610. Your method must return 0 because the last digit of 610 is 0.

def get_last_digit(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, index + 1):
            a, b = b, (a + b) % 10
        return b

print(get_last_digit(15))  # Output: 0