"""Задача: Move Zeroes (Переместить нули)
LeetCode №283"""

def move_zeroes(nums):
    if not nums:
        return 0
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i], nums[last_non_zero]= nums[last_non_zero], nums[i]
            last_non_zero+=1
    return nums


nums = [0, 1, 0, 3, 12]

print(move_zeroes(nums))