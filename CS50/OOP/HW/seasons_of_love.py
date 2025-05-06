import re
import sys
from datetime import date
import inflect

def main():
    number = get_minutes()
    p = inflect.engine()
    print(f'{p.number_to_words(number).capitalize().replace(' and ',' ')} minutes')

def get_minutes():
    input_date = is_valid(input("Date of Birth: "))
    delta = date.today() - input_date
    days = abs(delta.days)
    minutes = days*24*60
    return minutes


def is_valid(text):
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    if re.match(pattern, text):
        try:
            return date.fromisoformat(text)
        except ValueError:
            sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
