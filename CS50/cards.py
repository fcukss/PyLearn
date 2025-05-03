import random

cards = ['jack', 'queen', 'king']


def main():
    random.seed(0)  #ограничивает рандомность
    print(random.choice(cards))  #берет лист и возрашает рандомный элемент
    print(random.choices(cards, k=2)) #тоже самое только возврашает 2 карты(возможно совпадение карт так ка кон не убирает первый элемент)
    print(random.sample(cards, k=2))  #return different cards


main()