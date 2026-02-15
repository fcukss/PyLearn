def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        res = arr[mid]
        if res == target:
            return mid
        # Значение слишком большое, ищем в левой половине
        if res > target:
            high = mid - 1
        else:
            # Значение слишком маленькое, ищем в правой половине
            low = mid + 1
    # Если ничего не нашли
    return -1


my_list = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"Индекс числа 9: {binary_search(my_list, 9)}")  # Должно быть 4
print(f"Индекс числа 2: {binary_search(my_list, 2)}")  # Должно быть -1
