print(10,20,30,40)   #10 20 30 40
print(10,20,30,40, sep='')   #10203040

print(10,20,30,40, end='\n') #переход на след строчку. значение по default
print(10,20,30,40, end=' ') #не переходит на след строку
print("hello", "world", end ="*")

print()


import math
from math import trunc
num1 = 10.5
num2 = 12.6
num3 = 12.45665110
print(math.floor(num1)) #10

print(trunc(num2))  #12

print(round(num3,2))   #12.46

name = "Stanislav"
print(name[0])  #S
print(name[-1]) #V

print("h" in name)   #False
print("h" not in name)  #True

print("____________")
name = "John"
name1 = 'John'
name2 = 'john'

print(name==name1)  #True
print(name==name2)  #False

print("____________")

name = "Stanislav"
print(name[0:3])    #Sta
print(name[2:5])    #ani
print(name[:3])     #Sta
print(name[3:]) #nislav

print(name[::2])  #Sailv  каждій второй символ
print(name[1::2]) #tnsa каждій второй символ начиная с индекса[1]
print(name[::-1])  #valsinatS


print("____________")

word = "hello"
print(word.count("l"))  #2
print(word.replace('l','6'))  #he66o

word1 ="Hello"
print(word1.swapcase()) #hELLO

text = "Hello world"
print(text.find('l'))   #2
print(text.find('l',5))   #9
print(text.find('l',5,7))   #-1  element not found
print(text.find('x'))   #-1  element not found

print("____________")

text = "Hello world"
print(text.index('l'))   #2
print(text.index('l',5))  #9
# print(text.index('l',5,7))  #ValueError

print("____________")

word1 ="Hello"
print(word1.zfill(10))  #00000Hello

print("____________")

word1 ="  Hello  "
print(word1.strip())  #Hello

print("____________")

age = 37
name = "Stas"
print("my name is " + name + " and age " + str(age))

print("my name is {} and age {}".format(name,age))
print("my name is {0} and age {1}".format(name,age))
print(f"my name is {name} and age {age}")

print("____________")

a = 1/6
b = 1/3
print(a)  #0.16666666666666666
print(b)  #0.3333333333333333

print(f"{a:.2f}") #0.173
print("____________")

text = "hello"
print(text.isalpha())  #True
text1 = "123"
print(text1.isalpha())  #false

text = "hello1233"
print(text.isalnum())  #True
text1 = "123"
print(text1.isalnum())  #True

