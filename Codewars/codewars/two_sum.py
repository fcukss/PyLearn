#Write a function that takes an array of numbers (integers for the tests) and a target number. 
# It should find two different items in the array that, when added together, 
# give the target value. The indexes of these items 
# should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

def two_sum(numbers, target):
    num_dict = {}
    for i, num in enumerate(numbers):
        print(f'i = {i}, num  = {num}')
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []


print(two_sum([2,7,11,15], 9)) # returns [0,1]