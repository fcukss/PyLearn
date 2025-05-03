
def give_change(amount):
    bills = [1, 5, 10, 20, 50, 100]
    res = [0] * len(bills)
    for i in range(len(bills)-1,-1,-1):
        res[i] = amount // bills[i]
        amount %= bills[i]

    return tuple(res)


def give_change2( money ):
    arr = []
    for i in [100, 50, 20, 10, 5, 1]:
        arr = [money // i] + arr
        money -= arr[0] * i
    return tuple(arr)



print(give_change2(265))
