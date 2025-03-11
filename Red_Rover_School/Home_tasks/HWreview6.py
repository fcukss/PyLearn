# """
# Between Extremes
#
# Given an array of numbers, return the difference between the largest and smallest values.
# """
#
#
# def between_extremes(numbers):
#     if not numbers or len(numbers)==1:
#         return 0
#     return max(numbers)-min(numbers)
#
#
# numbers = [23, 3, 19, 21, 16]
# print(between_extremes(numbers))



"""
Complete the function that takes a sequence of numbers as single parameter.
 Your function must return the sum of the even values of this sequence.

Only numbers without decimals like 4 or 4.0 can be even.
"""


def sum_even_numbers(seq):
    if not seq:
        return 0
    return sum(list(filter(lambda x:  x % 2 == 0, seq)))

numbers = [4, 3, 1, 2, 5, 10, 6, 7, 9, 8]
print(sum_even_numbers(numbers))



"""
Largest Elements
Write a program that outputs the top n elements from a list.
"""

def largest(n, xs):
    new_arr = sorted(xs)
    if n==0:
        return []
    return new_arr[-n:]

"""
Create a function that will take any amount of money and break 
it down to the smallest number of bills as possible. 
Only integer amounts will be input, NO floats. 
This function should output a sequence, where each element 
in the array represents the amount of a certain bill type. 
The array will be set up in this manner:

array[0] ---> represents $1 bills

array[1] ---> represents $5 bills

array[2] ---> represents $10 bills

array[3] ---> represents $20 bills

array[4] ---> represents $50 bills

array[5] ---> represents $100 bills

In the case below, we broke up $365 into 1 $5 bill, 1 $10 bill, 1 $50 bill, and 3 $100 bills:
"""


def give_change(amount):
    bills = [1, 5, 10, 20, 50, 100]
    res = [0] * len(bills)
    for i in range(len(bills)-1,-1,-1):
        res[i] = amount // bills[i]
        amount %= bills[i]

    return tuple(res)