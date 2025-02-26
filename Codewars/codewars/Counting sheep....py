# def count_sheeps(sheeps):
#     if not sheeps:
#         return None
#     count = 0
#     for i in sheeps:
#         if i:
#             count+=1
#     return count

#var2
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)

array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]
arr=[]
print(count_sheeps(arr))
