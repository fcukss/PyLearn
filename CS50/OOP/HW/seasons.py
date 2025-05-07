import sys
from datetime import date
import inflect

def main():
    number = get_minutes()
    p = inflect.engine()
    print(f'{p.number_to_words(number).capitalize().replace(' and ',' ')} minutes')

def get_minutes():
    input_date = is_valid(input("Date of Birth (YYYY-MM-DD): ").strip())
    delta = date.today() - input_date
    return abs(delta.days) * 24 * 60


def is_valid(text):
    try:
        return date.fromisoformat(text)
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
