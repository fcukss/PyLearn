
def sum_even_numbers(seq):
    if not seq:
        return 0
    return sum(list(filter(lambda x:  x % 2 == 0, seq)))

numbers = [4, 3, 1, 2, 5, 10, 6, 7, 9, 8]
print(sum_even_numbers(numbers))
