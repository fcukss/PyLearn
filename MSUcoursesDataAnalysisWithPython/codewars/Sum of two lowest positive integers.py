def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0]+numbers[1]

#var2
# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])

numbers = [19, 5, 42, 2, 77]
print(sum_two_smallest_numbers(numbers))