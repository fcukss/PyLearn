#Write a function that takes an array of numbers (integers for the tests) and a target number. 
# It should find two different items in the array that, when added together, 
# give the target value. The indexes of these items 
# should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

def two_sum(numbers, target):
    num_dict = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i
    return None


print(two_sum([1, 2, 3], 4)) # returns (0, 2) or (2, 0)