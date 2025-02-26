
grocery_list = ['bread', 'milk', 'cheese']

#add meat to our list
grocery_list.append('meat')
print(grocery_list)

#возвращает последний индес и убирает из листа єтот єлемент
x = grocery_list.pop()
print(x)                 #meat
print(grocery_list)      #['bread', 'milk', 'cheese']

#delete element from list
grocery_list.remove('milk')
print(grocery_list)    #['bread', 'cheese']


