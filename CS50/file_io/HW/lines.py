import sys
import os

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file = sys.argv[1]

    if not file.endswith(".py"):
        sys.exit("Not a Python file")

    if not os.path.isfile(file):
        sys.exit("File does not exist")

    try:
        with open(file, 'r', encoding="utf-8") as f:
            count = 0
            for line in f:
                stripped = line.strip()
                if not stripped:
                    continue
                if stripped.startswith("#"):
                    continue
                count += 1
            print(count)
    except Exception as e:
        sys.exit(f"Error reading file: {e}")

if __name__ == "__main__":
    main()