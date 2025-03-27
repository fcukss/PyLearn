#create exception
class FirstNameError(Exception):
    pass



def greet(name):
    if not isinstance(name, str):
        raise TypeError("no correct type")

    if not name.isalpha():
        raise FirstNameError(f"{name}  - not the name")

    print(f"hi, {name}")

greet("123")