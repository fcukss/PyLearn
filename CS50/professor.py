import random


def main():
    level = get_level()
    count_res = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        attemps = 0

        while attemps < 3:
            try:
                res = int(input(f"{x} + {y} ="))
                if res == z:
                    count_res += 1
                    break
                else:
                    print('EEE')
            except ValueError:
                print('EEE')

            attemps += 1

        if attemps == 3:
            print(f"{x} + {y} = {z}")

    print(f"Score: {count_res}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
