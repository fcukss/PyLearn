def transpose_two_strings(arr):
    max_length = max(len(arr[0]), len(arr[1]))

    res = ''
    for i in range(max_length):
        char_1 = ' '
        if i < len(arr[0]):
            char_1 = arr[0][i]
        if i < len(arr[1]):
            char_2 = arr[1][i]
        else:
            char_2 = ' '
        res += char_1 + ' ' + char_2
        if i != max_length-1:
            res+='\n'
    return res