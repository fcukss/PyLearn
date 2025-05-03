import csv
import sys
import os
from tabulate import tabulate


def main():
    # if len(sys.argv) < 2:
    #     sys.exit("Too few command-line arguments")
    # elif len(sys.argv) > 2:
    #     sys.exit("Too many command-line arguments")
    # file = sys.argv[1]
    # if not file.endswith(".csv"):
    #     sys.exit("Not a CSV file")
    #
    # if not os.path.isfile(file):
    #     sys.exit("File does not exist")
    try:
        with open('regular.csv') as file:
            reader = csv.reader(file)
            headers = next(reader)
            print(tabulate(reader, headers, tablefmt="grid"))
    except FileNotFoundError as e:
        ...


main()
