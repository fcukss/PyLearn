"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


def twoSum(nums : list, target : int)-> list:
    res=[]
    for i in range(len(nums)):
        if nums[i]+nums[i+1]==target:
            res.append(i)
            res.append(i+1)
            return res
nums = [3,2,4]
target = 6
print(twoSum(nums,target))