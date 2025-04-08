

# #=================WRITE IN FILE==============================
# name = input("What's your name? ")
# # # w - файл в режими записи (при повторном открітии он перезаписівается)
# # file = open("names.txt","w")
# # a - append добавляет в файл
# with open("names.txt","a") as file:   #автомтически закрывает файл
#     #записывает каждое имя с новой строки
#     file.write(f"{name}\n")



#=====================READ THE FILE=============================

# with open("names.txt",'r') as file:
#     lines = file.readlines()
# print(lines)  #['Tom\n', 'bill\n', 'Anna\n', 'Neo\n']
# for line in lines:
#     print("Hello,",line.rstrip())

# #упрощаем код
# with open("names.txt",'r') as file:
#     for line in file:
#         print("Hello,", line.rstrip())

#делаем сортировку можно так можно собрать в лист и потм его использовать
with open("names.txt") as file:
    for line in sorted(file, reverse=True):  #сортируем в обратном порядке
        print("hello,", line.rstrip())


