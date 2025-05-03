import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'^\s*(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s*$'
    match = re.match(pattern, s.strip(), re.IGNORECASE)
    if not match:
        raise ValueError("Invalid time format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    def to_24_hour(hour, minute, period):
        hour = int(hour)
        minute = int(minute) if minute else 0
        if not (0 <= minute < 60):
            raise ValueError("Invalid minute value")
        period = period.upper()
        if period == 'AM':
            if hour == 12:
                hour = 0
        elif period == 'PM':
            if hour != 12:
                hour += 12
        else:
            raise ValueError("Invalid period")
        return f"{hour:02d}:{minute:02d}"

    start = to_24_hour(h1, m1, p1)
    end = to_24_hour(h2, m2, p2)

    return f"{start} to {end}"


if __name__ == "__main__":
    main()


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    try:
        convert("9:60 AM to 5:60 PM")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid minutes"

    try:
        convert("9AM to 5PM")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for missing space before AM/PM"

    try:
        convert("9 AM - 5 PM")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid format"

    try:
        convert("09:00 AM - 17:00 PM")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid format"
