import re

def main():
    color  = input("Hexadecimal color code: ")
    pattern = r"^#[0-9a-fA-F]{6}$"
    match = re.search(pattern, color)
    if match:
        print(f'Valid. Matched with {match.group()}')
    else:
        print("Invalid")

if __name__ == '__main__':
    main()