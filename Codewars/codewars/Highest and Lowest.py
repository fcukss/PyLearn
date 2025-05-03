def high_and_low(numbers):
    lst = list(map(int, numbers.split(" ")))
    return f'{max(lst)} {min(lst)}'

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

# assert high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9"
# assert high_and_low("1 2 -3 4 5") == "5 -3"
# assert high_and_low("1 9 3 4 -5") == "9 -5"