import re

def main():
    print(parse("http://youtube.com/embed/xvFZjo5PgG0"))


def parse(s):
    match = re.search(r"^https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})",s)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    return None



if __name__ == "__main__":
    main()


def test_parse():
    assert parse("http://youtube.com/embed/xvFZjo5PgG0") == "https://youtu.be/xvFZjo5PgG0"
    assert parse("http://youtube.com/embed/xvFZjo5PgG0") == "https://youtu.be/xvFZjo5PgG0"
    assert parse("https://youtube.com/embed/xvFZjo5PgG0") == "https://youtu.be/xvFZjo5PgG0"
    assert parse("https://www.youtube.com/embed/xvFZjo5PgG0") == "https://youtu.be/xvFZjo5PgG0"