def all_non_consecutive(arr):
    lst=[]
    for i,n in enumerate(arr[1::]):
        if n - arr[i]!=1:
            lst.append({'i':i+1, 'n':n})
    return lst








numbers = [1,2,3,4,6,7,8,15,16]

print(all_non_consecutive(numbers))
