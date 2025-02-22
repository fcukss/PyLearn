"""Task 1
even or odd
"""
#
# print("enter a number: ")
# n = int(input())
# if n % 2 == 0:
#     print(f"число {n} - четное")
# else:
#     print(f"число {n} - нечетное")
#
# print("+++++++++++++++++++")

"""
Task 2
"""

# print("введите день недели")
# day = input().lower()
# if day == "saturday" or day == "sunday":
#     print("today is holiday")
# elif day == 'wednesday':
#     print("Мне сегодня к стоматологу в 15:30")
# else:
#     print("working day")

"""
Task 3
Программа должна вывести вашу строку text на экран n-раз
"""
# print("enter num")
# n = int(input())
# print("enter text")
# text = input()
#
# for i in range(n):
#     print(text)

"""
Task 4
Программа должна вывести на экран количество 
гласных букв в строке message
"""
# print("введите текст на рус")
# message = input()
#
# count = 0
# for c in message:
#     if c in'ауоиэыяюеё':
#         count+=1
# print(count)
#

"""
Task5
sum
"""

print("enter number:")
n = int(input())

while True:
    print("enter number:")
    a=int(input())
    if a>0:
        n+=a
    else:
        break
print(n)
