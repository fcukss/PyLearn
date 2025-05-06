# def is_triangle(a, b, c):
#     if a | b | c == 0:
#         return False
#     if (a + b > c) and (a + c > b) and (c + b > a):
#         return True
#     else:
#         return False
#
#
# print(is_triangle(7,2,2))


def pipe_fix(nums):
    res = []
    for i in range(nums[0], nums[len(nums)-1]+1):
        res.append(i)
    return res

n = [1, 2, 3, 4, 5, 6, 7, 8]
print(pipe_fix(n))
