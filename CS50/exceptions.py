def get_int(promt):
    while True:
        try:
            return int(input(promt))
        except ValueError:
           pass
            # print("x is not integer")



def main():

    x = get_int("What is x? ")
    print(f"x is {x}")

main()

