def binary_array_to_number(arr):
    str_list = map(str, arr)
    return int("".join(str_list),2)

        
print(binary_array_to_number([0, 0, 0, 1]))
#Testing: [0, 0, 0, 1] ==> 1
#Testing: [0, 0, 1, 0] ==> 2