"""
There is a naughty number hidden somewhere in the list.
 Find the index of it, if you are strong enough, of course!

Input:
You will receive an array of arrays (a list of lists).
Each sub-array can only contain either another array or a single number.
There will always be at least one sub-array in the input.
There will be only one number hidden in the sub-arrays
Output:
Return the index of the first-level sub-array that contains the hidden number.
"""



def find_hidden_number_index(nested_list):
    for index, sub_array in enumerate(nested_list):
        if isinstance(sub_array, list) and len(sub_array) == 1:
            element = sub_array[0]
            while isinstance(element, list) and len(element) == 1:
                element = element[0]
            if isinstance(element, (int, float)):
                return index
    return None


n = [[[[]]] , [[]], [], [], [[100]] ]
a = [ [], [8], [] , [] ]

print(find_hidden_number_index(n))  #4
nested_list = [[[]], [[42]], [[]]]
