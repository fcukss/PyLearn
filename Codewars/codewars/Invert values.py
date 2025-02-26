def invert(lst):
    i=[]
    for x in lst:
        i.append(x*-1)
    return i

n = [2,3,4]
print(invert(n))