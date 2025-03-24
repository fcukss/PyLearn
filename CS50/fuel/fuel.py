def main():
    while True:
        try:
            fraction = input("Fraction: ")
            res = gauge(convert(fraction))
            print(res)
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = map(int, fraction.split("/"))
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    percentage = round((x / y) * 100)
    return percentage

def gauge(percentage):
    if percentage >=99:
        return 'F'
    if percentage<= 1:
        return 'E'
    else:
        return f"{percentage}%"

if __name__ == '__main__':
    main()
