from platform import android_ver
from traceback import print_tb

print("Hello world")
print('Hello')

x=1
y=2
print(x,y)
print("----------------------------")

a=1
b=2

c=a/2
print(c)        #0.5
c=a//2
print(c)        #0
c=a%2
print(c)        #1


print("----------------------------")

x,y=y,x
print(x,y)
print("----------------------------")
a=10
while a>0:
    a-=1
    print(a)
    if a==5:
        break
else:
    a == 1
    print("stop")
print("----------------------------")
n=1
for n in 1,2,3:
    print(n**2)              #1,4,9
print("----------------------------")
c=1
for c in range(1,10,2):
    print(c**1)                 #1,3,5,7,9

print("----------------------------")

name1="python"
name2= 'python'

print(type(name1))
print(type(name2))
print("----------------------------")
#
# a=1
# b=3
# sum=a+b
# print("a"," + ", "b", " = ", sum)
# print("a"," + ", "b", " = ", sum,sep="/")
# print("----------------------------")
#
# a=input()
# b=input()
# sum=a+b
# print(sum)   #4050 это строка
# print("------------")
# a=int(input())
# b=int(input())
# sum2=a+b
# print(sum2) #90 это число

print("----------------------------")

print(int(12.6))   #12
print(float(10.5656))

print("----------------------------")
print(5==4)  #False
print(5!=5)  #False
print(5==5)  #True

