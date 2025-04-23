def is_ascending(lst):
    for i in range(1, len(lst)):
        if lst[i]<= lst[i-1]:
            return False
    return True


assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False
assert is_ascending([1, 3, 3, 5]) == False