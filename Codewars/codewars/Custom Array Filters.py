"""
Dave has a lot of data he is required to apply filters to,
 which are simple enough, but he wants a shorter
 way of doing so.

He wants the following functions to work as expected:
even # list([1,2,3,4,5]).even() should return [2,4]
odd # list([1,2,3,4,5]).odd() should return [1,3,5]
under # list([1,2,3,4,5]).under(4) should return [1,2,3]
over # list([1,2,3,4,5]).over(4) should return [5]
in_range # list([1,2,3,4,5]).in_range(1, 3) should return [1,2,3]
"""

arr = [1,2,3,4,5]

def list(arr):
    if not arr:
        return -1
    return arr

def even():
    new_arr=[]
    for num in arr:
        if num % 2 != 0:
            new_arr.append(num)



def odd():
    ...


def under(number):
    ...


def over(number):
    ...


def in_range():
    ...


