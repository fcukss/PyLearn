import validator_collection

def main():
    print(is_valid_email(input("What's your email address? ")))

def is_valid_email(text):
    return validator_collection.is_email(text)


def test_is_valid():
    assert is_valid_email('staskapl@gamil.com') == True
    assert is_valid_email('staskapl@com') == False
