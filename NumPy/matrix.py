import numpy as np
from numpy import dtype

matrix = np.array([(1, 2, 3), (4, 5, 6)], dtype = np.float64)
print(matrix)
print(matrix.shape) #(2, 3)
print(matrix.ndim)  #2
print(matrix.size) # 6 elements in matrix

res = matrix.reshape(1, 6)
print(res)  #[[1. 2. 3. 4. 5. 6.]]

matrix2 = np.eye(5)
print(matrix2)  #[[1. 0. 0. 0. 0.]
                   # [0. 1. 0. 0. 0.]
                   #  [0. 0. 1. 0. 0.]
                    # [0. 0. 0. 1. 0.]
                    #    [0. 0. 0. 0. 1.]]


#fill the matrix with 9
matrix3 = np.full((3,3),9)
print(matrix3)

##############################################
#axis  - ось 0 - ось строк, ось 1 - ось столбцов
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#delete 1st string from the matrix (second string)
res = np.delete(matrix, 1, axis = 0)
print(res)

#delete 1st row from the matrix (second row)
res = np.delete(matrix, 1, axis = 1)
print(res)

summa = matrix.sum()
print(summa) #45
print(matrix.max())  #9
print(matrix.max(axis=0))  #[7 8 9]
print(matrix.max(axis=1)) #[3 6 9]

#среднее значение по строкам (1+4+7)/3 = 4 и тд
res = np.mean(matrix, axis = 0)
print(res)   #[4. 5. 6.]


#concate matrixes
matrix = np.array([(1, 2, 3), (4, 5, 6)])
matrix2 = np.array([(7, 8, 9), (10, 11, 12,12)])
#по столбцам
res = np.concatenate((matrix, matrix2), axis = 1)
print(res) #[[ 1  2  3  7  8  9]
            #[ 4  5  6 10 11 12]]
#по строкам
res = np.concatenate((matrix, matrix2), axis = 0)
print(res) #[[ 1  2  3]
            #[ 4  5  6]
            #[ 7  8  9]
            #[10 11 12]]


###
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
res = matrix.flatten()
print(res)   #[1 2 3 4 5 6 7 8 9]


##
matrix = np.array([[1, 2], [3, 4], [5, 6]])
res = matrix.reshape(2, 3)
print(res)    #[[1 2 3]
              #[4 5 6]]

print("____________________")
#############################
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.array([[a,b], [b,a]])
print(c)

print("____________________")

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

res = np.stack([arr1, arr2], axis = 2)
print(res)