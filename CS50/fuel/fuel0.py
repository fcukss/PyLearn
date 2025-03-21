def fuel():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split("/"))
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            percentage = round((x / y) * 100)
            if percentage >=99:
                return 'F'
            if percentage<= 1:
                return 'E'
            else:
                return f"{percentage}%"
        except (ValueError, ZeroDivisionError):
            pass

print(fuel())