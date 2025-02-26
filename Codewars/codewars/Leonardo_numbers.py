"""
каждый следующий элемент последовательности
равен сумме двух предыдущих элементов плюс единица.
Первые несколько чисел Леонардо: 1, 1, 3, 5, 9, 15, 25, 41
и так далее.
"""

def leonardo_numbers(n, L0, L1, add) :
    arr =[]
    arr.append(L0)
    arr.append(L1)

    for i in range(1,n-1):
        print(i)
        arr.append(arr[i-1]+arr[i]+add)
    return arr


print(leonardo_numbers(5, 1, 1, 1))




