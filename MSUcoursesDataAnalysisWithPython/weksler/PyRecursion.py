"""
рекурсивная функция
"""
#
# def get_age():
#     value = input("Enter your age ")
#     try:
#         value = int(value)
#         return value
#     except Exception as e:
#         print(f"You enter uncorrect age. Error {e}")
#         return get_age()
#
# age = get_age()
# print(f"Your age is {age}")
print("_____________________________")

def factorial(n):
    if n ==1:
        return 1
    return n * factorial(n-1)

res = factorial(3)
print(res)