import test


def mirror(data: list) -> list:
    arr = sorted(data)
    return arr + arr[-2::-1]



nums = [1, 2, 3]
print(mirror(nums))


print(nums[-2::-1])



