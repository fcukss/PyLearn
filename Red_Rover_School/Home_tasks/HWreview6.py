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

"""
How many consecutive numbers are needed
Write a function that takes an array of unique integers and returns
 the minimum number of integers needed to make the values of the array 
 consecutive from the lowest number to the highest number.
"""

def consecutive(arr):
    if not arr:
        return 0
    new_arr = sorted(arr)
    for i in range(min(arr)+1,max(arr)):
        new_arr.append(i)
    return len(set(new_arr))-len(arr)



def consecutive2(arr):
    return abs(len(arr)-(max(arr)-min(arr)))+1


"""
Trimming a string

Create a function that will trim a string (the first argument given) if it is longer than the requested maximum string length (the second argument given). The result should also end with "..."

These dots at the end also add to the string length.

For example, trim("Creating kata is fun", 14) should return "Creating ka..."

If the string is smaller or equal than the maximum string length, then simply return the string with no trimming or dots required.

e.g. trim("Code Wars is pretty rad", 50) should return "Code Wars is pretty rad"""


def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    elif size <= 3:
        return phrase[:size] + '...'
    else:
        return phrase[:size - 3] + '...'



"""
Find all non-consecutive numbers
"""