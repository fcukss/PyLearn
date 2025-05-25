def sort_array(arr):
    odds = []
    for i in arr:
        if i%2!=0:
            odds.append(i)
    odds.sort()
    odd_index=0
    res = []
    for n in arr:
        if n%2!=0:
            res.append(odds[odd_index])
            odd_index+=1
        else:
            res.append(n)
    return res




def test_arr():
    assert sort_array([7,1]) == [1,7]
    assert sort_array([5, 8, 6, 3, 4]) == [3, 8, 6, 5, 4]
    assert sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]