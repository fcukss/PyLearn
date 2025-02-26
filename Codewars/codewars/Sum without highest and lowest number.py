"""

Sum all the numbers of a given array ( cq. list ),
except the highest and the lowest element
( by value, not by index! ).

The highest or lowest element respectively is
a single element at each edge,
even if there are more than one with the same value.

"""

def sum_array(arr):
    if not arr:
        return 0
    arr.sort()
    return sum(arr[1:-1:])


n = [6, 2, 1, 8, 10]
print(sum_array(n))
