import numpy as np


# np_ can contain only one datetype.

#create np arrays
data = [1,2,3,4]
arr = np.array(data) #create np array from list
print(arr)
print(arr.shape) #размерность массива 1D (4,)
print(arr.dtype)  #data type int64
print(arr.ndim) # 1 глубина

######################################333333

arr2 = np.array([1,2,3,4], dtype=np.float64)
print(arr2)
print(arr2.dtype)
#######################################
#create zero matrix
print('create zero matrix')
a = np.zeros((5,3))

print(a.dtype)

###############################
#create arrange array with step 0.5

arr3 = np.arange(0,20,0.5)
print(arr3)

# 5 числе от 0 до 2
arr4 = np.linspace(0,2,5)
print(arr4)   #[0.  0.5 1.  1.5 2. ]

#random
random_arr = np.random.random(5)
print(random_arr)
print(f"random_arr.dtype= {random_arr.dtype}")

##############################################
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

c =  a + b
print(c)   #[ 7  9 11 13 15]

a = a * 2 #умножаем все эдементы на 2. так же можно влзводить в степрь и тд.
print(a)   #[ 2  4  6  8 10]
###################################


arr5 = np.array([-1,2,-3,-4,0,-1,2,3,5,10])
res = arr5<2
print(res) #[ True False  True  True  True  True False False False False]

#indexes
arr = np.array([1,-2,3,-4,5])
print(arr[0:2])
print(arr[::-1])
#chose elements<2
print(arr[arr<2])   #[ 1 -2 -4]
print(arr[(arr<2) &(arr>0)])  #[1]
#занулить все жлементы от 1 до 4 индекса
arr[1:4] = 0
print(arr)   #[1 0 0 0 5]
##################################

print('DATATYPE')

arr = np.array([[6,0.3],[True, False]])
arr2 = np.array([78.009, True, 'sfsf'])
print(arr.dtype)
print(arr2.dtype)
#change datetype
new_arr = arr.astype(np.int32)
print(new_arr.dtype)