def consecutive(arr):
    if not arr:
        return 0
    new_arr = sorted(arr)
    for i in range(min(arr)+1,max(arr)):
        new_arr.append(i)
    return len(set(new_arr))-len(arr)

def consecutive(arr):
    return abs(len(arr)-(max(arr)-min(arr)))+1


arr = [4, 8, 6]

print(consecutive(arr))