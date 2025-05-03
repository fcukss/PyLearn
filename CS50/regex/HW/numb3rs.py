import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = re.compile(
        r'^('
        r'(25[0-5]|'        # Matches 250-255
        r'2[0-4][0-9]|'     # Matches 200-249
        r'1[0-9]{2}|'       # Matches 100-199
        r'[1-9]?[0-9])'     # Matches 0-99
        r'\.){3}'
        r'(25[0-5]|'
        r'2[0-4][0-9]|'
        r'1[0-9]{2}|'
        r'[1-9]?[0-9])$'
    )
    return bool(pattern.match(ip))


if __name__ == "__main__":
    main()

