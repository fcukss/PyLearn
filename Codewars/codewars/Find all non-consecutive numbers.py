def all_non_consecutive(arr):
    res={}
    lst=[]
    for i,n in enumerate(arr[1::]):
        if n - arr[i]!=1:
            res['i']=i+1
            res['n']=n
            lst.append(res)

    return lst








numbers = [1,2,3,4,6,7,8,15,16]

print(all_non_consecutive(numbers))
