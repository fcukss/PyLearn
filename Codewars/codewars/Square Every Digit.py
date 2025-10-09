#For example, if we run 9119 through the function, 
# 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)


def square_digits(num):
    return int(''.join(str(int(i)**2) for i in str(num)))

print(square_digits(765))  # 811181
