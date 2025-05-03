import csv
import sys


def main():

    # if len(sys.argv) < 3:
    #     sys.exit("Too few command-line arguments")
    # elif len(sys.argv) > 3:
    #     sys.exit("Too many command-line arguments")
    # before = sys.argv[1]
    # after = sys.argv[2]
    # if not os.path.isfile(before):
    #     sys.exit(f"Could not read {before}")

    # try:
    #     with (open(before, 'r', encoding='utf-8') as file,
    #           open(after, 'w', encoding='utf-8') as output):
    try:
        with (open("before.csv", 'r', encoding='utf-8') as file,
                open("after.csv", 'w', encoding='utf-8') as output):
            reader = csv.DictReader(file)
            writer = writer = csv.DictWriter(output, fieldnames=['first', 'last', 'house'])
            writer.writeheader()

            for row in reader:
                last, first = row['name'].strip().split(', ')
                writer.writerow({
                    'first': first,
                    'last': last,
                    'house': row['house']
                })
    except FileNotFoundError:
        ...# sys.exit(f"Could not read {before}")
    except KeyError:
        sys.exit("Input file missing expected columns")

main()