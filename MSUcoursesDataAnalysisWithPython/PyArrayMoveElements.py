
A = [0,1,2,3,4,5]

#сдвиг массива влево
temp=A[0]
n = len(A)
for i in range(n-1):
    A[i]=A[i+1]
A[n-1] = temp
print(A)

#сдвиг массива вправо
temp=A[n-1]
for k in range(n-2,-1,-1):
    A[k+1] = A[k]
A[0]=temp
print(A)