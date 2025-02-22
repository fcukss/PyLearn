"""Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k."""


def remove_duplicates(nums):
    if not nums:
        return 0

    # Инициализация указателя для уникальных элементов
    k = 0

    # Проходим по массиву с помощью второго указателя
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]

    # Количество уникальных элементов равно k + 1
    return k + 1

# Пример использования:
nums = [1, 1, 2, 2, 3, 4, 4, 5]
k = remove_duplicates(nums)
print(f"Количество уникальных элементов: {k}.")
print(f"Массив с уникальными элементами: {nums[:k]}")
