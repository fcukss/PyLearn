# # проверяем что среди чисел есть число которое делится на 10
# flag=False
# N=int(input())
# for i in range(N):
#     x=int(input())
#     flag=(x%10==0) or flag
#     print(flag)
#     break
#


# # проверяем что все числа делится на 10
#
# flag=True
# N=int(input())
# for i in range(N):
#     x=int(input())
#     flag= flag and x%10==0
# print(flag)

# добываем цифры из числа

base = 7
x= int(input())
while x>0:
    digit = x % base    #взять послдению цифру
    print(digit, end=' ')
    x//=base       #зачеркнуть последнию цифру