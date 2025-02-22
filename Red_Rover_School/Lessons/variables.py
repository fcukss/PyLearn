first_name = 'Anna'

print("Hello", first_name)  # Hello Anna
print("Hello" + first_name)  # HelloAnna

first_name = "Tom"
print("Hello", first_name)  # Hello Tom

a = 10
b = "5"
print(a + int(b))  # 15
a = int(10)

# ПРОВЕРКА НА ЧЕТНОСТЬ
def is_even(num: int) -> bool:
    return num & 1 == 0


def is_even2(num: int) -> bool:
    return not (num & 1)


print(is_even(10))
print(is_even2(10))
