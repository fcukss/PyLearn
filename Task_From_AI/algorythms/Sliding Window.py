"""
Maximum Average Subarray I (Максимальное среднее подмассива)
LeetCode №643
Условие: Дан массив nums и число k.
Нужно найти подмассив длиной ровно k,
у которого максимальное среднее арифметическое,
и вернуть это значение.
Пример:Вход: nums = [1, 12, -5, -6, 50, 3], k = 4
Выход: 12.75(Подмассив [12, -5, -6, 50] дает сумму 51.
51 / 4 = 12.75)
"""

def findMaxAverage(nums: list[int], k: int) -> float:

    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(k, len(nums)):
        current_sum = current_sum + nums[i] - nums[i-k]
        #проверем что больше и обновлем переменную max_sum
        max_sum = max(max_sum, current_sum)
    return max_sum/k

nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))


