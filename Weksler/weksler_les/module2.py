shopping_list = {
    "liver": 3,
    "carrot" : 2,
    "onion" : 1
}

print(shopping_list)
print(sum(shopping_list.values()))

#immurable
first_name = "Stas"

first_name.replace("S","T")

print(first_name)    #Stas

first_name = first_name.replace("S","T")
print(first_name)   #Tast

next_name = first_name.replace("S","T")
print(next_name)     #Tast

#mutable
names = ['Harry', 'Ron', 'Luke', 'Ron', 'Anna']
print(names)   #['Anna', 'Harry', 'Luke', 'Ron', 'Ron']

names.sort()
print(names)

#create set содержит уникальные значения
new_set = set(names)

print(new_set)  #{'Ron', 'Anna', 'Harry', 'Luke'}


shopping_list = {
    "liver": 3,
    "carrot" : 2,
    "onion" : 1,
    "potato": None
}


#tuple то что и лист только не изменяемый
#VAR1
names = ('Harry', 'Ron', 'Luke', 'Ron', 'Anna')
#vaR2
names_t = tuple(names)
print(names)