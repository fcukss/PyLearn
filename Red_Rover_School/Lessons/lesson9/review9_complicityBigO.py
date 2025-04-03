import copy
import time

# time O(1)
# def print_idx(arr:list, i:int):
#     start = time.time()
#     a = arr[i]
#     end = time.time()
#     print(f"{(end-start):.7f}")   #0.0000021
#
#     start = time.time()
#     # access to the last element
#     a = arr.pop()
#     end = time.time()
#     print(f"{(end-start):.7f}")    #0.0000014
#
#     start = time.time()
#     #пробегает по листу
#     a = arr.pop(i)
#     end = time.time()
#     print(f"{(end-start):.7f}")    #0.0011055
#
# print_idx([5,8,4,7,3,2,0]*100000,3)



# time O(log n)
arr = [i for i in range(67998, 1000000)]


def binary_search(arr, num):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == num:
            return m
        elif arr[m] < num:
            l = m + 1
        else:
            r = m - 1
    return -1


print(binary_search(arr, 70000))
