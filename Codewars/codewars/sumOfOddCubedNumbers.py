def cube_odd(arr):
    new_arr =[]
    for i in arr:
        if type(i) is not int:
            return None
        if i %2!=0:
            new_arr.append(i**3)
    return sum(new_arr)

def test_cube():
    assert cube_odd([1, 2, 3, 4])== 28
    assert cube_odd([-3,-2,2,3]) == 0
    assert cube_odd(["a", 12, 9, "z", 42]) is None
    assert cube_odd([True, False, 3, 4]) is None