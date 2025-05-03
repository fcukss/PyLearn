def spacey(array):
    res = []
    s = ''
    for item in array:
        s+=item
        res.append(s)
    return res



arr=['i', 'have','no','space']
print(spacey(arr))