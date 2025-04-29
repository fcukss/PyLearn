import re

def main():
    print(count(input("Text: ")))


def count(text):
    matches = re.findall(r'\bum\b', text.lower())
    return len(matches)



if __name__ == "__main__":
    main()



def test_count():
    assert count('um') ==1
    assert count('um?') == 1
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2