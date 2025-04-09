import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    pattern = ".py"
    file = sys.argv[0]
    if pattern in file:
        try:
            with open(file, 'r', encoding="utf-8") as f:
                contents = f.readlines()
                print(len(contents) + 1)
        except:
            sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

if __name__ == '__main__':
    main()