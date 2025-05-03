import random


def game():
    x=0
    while x==0:
        try:
            level = int(input("Level "))
            if 0<level<100:
                number = random.randrange(1, level)
                while True:
                    guess = int(input("Guess "))
                    if guess > number:
                        print("Too large!")
                        continue
                    if guess < number:
                        print("Too small!")
                        continue
                    else:
                        print("Just right!")
                        x=1
                        break
        except (ValueError):
            pass


game()
