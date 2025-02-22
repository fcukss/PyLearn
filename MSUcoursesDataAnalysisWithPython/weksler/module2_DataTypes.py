"""
преобразование типов
"""
#convert string to int
age = "35"
age = int(age)
new_age = age + 1
print(new_age)

#convert int to string
age = 33
age = str(age)   #<class 'str'>

#convert string to List
name =  "Stas"
name = list(name)  #['S', 't', 'a', 's']
print(name)

#int нельзя преобразовать в list но
age = 40
age = str(age)
age = list(age)

print(age)  #['4', '0']
