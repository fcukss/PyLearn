import re
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalpha() and 2<len(s)<=6:
        return True
    pattern = r"^[A-Z]+[1-9][0-9]*$"
    return bool(re.fullmatch(pattern, s))

if __name__ == '__main__':
    main()

