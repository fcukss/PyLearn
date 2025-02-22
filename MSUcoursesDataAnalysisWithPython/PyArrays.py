#
# A = [100,200,300,400,500]
#
# for x in A:
#     print(x, type(x))
#     x+=1
#     print(x)
# print("----------------------------")
#
# #меняем элементы массива
# for k in range(5):
#     A[k]=A[k]*A[k]
# print(A)   #[10000, 40000, 90000, 160000, 250000]
#
# print("----------------------------")
#
# #заполняем массив
# A=[0]*1000  #create array with 1000 elements
# print(A)
# print(len(A))   #length of array
# print("----------------------------")
#
# N = int(input())
# A=[0]*N
# B=[0]*N
# x=0
# for k in range(len(A)):
#     A[k]=x
#     x+=5
# print("A=",A)
# # copy A to B
# for k in range(N):
#     B[k]=A[k]
#
# print("B=",B)
# C=A     #create link C for Array A
# D=list(A)  #create copy of Array A
# print("C=",C)
# A[4]=100
# print("A=",A)
# print("C=",C)   # это ссылка на массив А
# print("B=",B)   # это отдельный массив B
# print("D=",D)   # это отдельный массив D
# print("----------------------------")
#
#
# for i in range(1,6):
#     print('*' * i)
# print("---------------")
#
# for i in range(1,6):
#     for j in range(i):
#         print('*', end='')
#     print()
# print("---------------")

"""найдем элементы массива начинающиеся на А"""

names = ["Tom", "Anna", "Bill", "Adam", "Jerry"]
starts_a = []
for name in names:
    if name.startswith("A"):
        starts_a.append(name)
print(starts_a)  # ['Anna', 'Adam']

# var2
names = ["Tom", "Anna", "Bill", "Adam", "Jerry"]
starts_a = [name for name in names if name.startswith("A")]
print(starts_a)  # ['Anna', 'Adam']

# var3
names = ["Tom", "Anna", "Bill", "Adam", "Jerry"]
starts_a = filter(lambda name: name.startswith("A"), names)
print(tuple(starts_a))  # ('Anna', 'Adam')

# MAKE A DIFFERENT COPY OF ARRAY

numbers = [1, 50, 60, 20]
another_numbers = numbers
another_numbers.append(100)
print(another_numbers)  # [1, 50, 60, 20, 100]
print(numbers)  # [1, 50, 60, 20, 100]

another_numbers = numbers[:]  # copy of massive
another_numbers.append(200)
print(another_numbers)  # [1, 50, 60, 20, 100, 200]
print(numbers)  # [1, 50, 60, 20, 100]

print("---------------")

a = b = c = d = True

if a and b and c and d:
    print("all True")
#проверяем что все True
if all((a,b,c,d)):
    print("all True")

#check if one of them is True
if any((a,b,c,d)):
    print("any True")

