# import random
#
# coin = random.choice(["орел", "решка"])
# print(coin)
#
# #generate the number in range 1-10
# number = random.randint(1,10)
# print(number)
#
# #перемешивает значения в листах
# cards = ["jack",'quenn',"king"]
# random.shuffle(cards)
# print(cards)
#
# print("__________________________________________________")
#
# import statistics
#
# #generate avarage number
# print(statistics.mean([100,105]))
#
# print("__________________________________________________")
#
# import sys
#
# #запускаем программу через терминал и вводим свое имя
#
# #check for errors
# if len(sys.argv) <2:
#     sys.exit("Too few arguments")
#
# #Print name tags
# for arg in sys.argv[1;]:
#     print("hello, my name is ", arg)
# print("__________________________________________________")


import cowsay
import sys


if len(sys.argv)==2:
    # cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])