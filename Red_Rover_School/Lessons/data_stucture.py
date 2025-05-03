# a = [1,2,3]
# b = [1,2,3]
#
# print(a == b)  #True
# print(a is b)  #False проверяет на одинаковость обьектов
# from os import remove

#++++++++++++++++++SET+++++++++++++

# #set = {} # нельзя так соset = set() # create set
# set.add(3)
# set.add(4)
# set.add(4)
# set.add(5)
# print(set)   #{3, 4, 5}
#
# здать сет


arr = ['a', 'b', 'c', 'd', 'e','i','b']
for i in arr:
    if i=='b':
        arr.remove(i)
    else:
        print(i)
print(arr)


