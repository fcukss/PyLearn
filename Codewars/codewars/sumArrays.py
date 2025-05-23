def sum_array(a):
    return sum(a)


def test_sum_array():
    assert sum_array([1, 5.2, 4, 0, -1]) == 9.2
    assert sum_array([]) == 0
    assert sum_array([-2.398]) == -2.398
    assert sum_array([1, 2, 3, 4, 5]) == 15


