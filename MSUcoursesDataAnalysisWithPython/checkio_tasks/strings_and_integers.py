def first_word(text: str) -> str:
    a = text.rsplit()
    return a[0]


print(first_word("Hello world"))

print("_________________________________")


def number_length(value: int) -> int:
    return len(str(value))


print(number_length(0))
print("_________________________________")

""""Fizz buzz" це гра зі словами, за допомогою якої ми будемо вчити наших роботів діленню. Давайте навчимо комп'ютер.

Ви повинні написати функцію, параметр якої є позитивне ціле число, функція повинна повертати:
"Fizz Buzz", якщо число ділиться на 3 та на 5;
"Fizz", якщо число ділиться тільки на 3;
"Buzz", якщо число ділиться тільки на 5;
Число, у вигляді рядка для інших випадків
"""


def checkio(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


print(checkio(10))

print("_________________________________")

"""Ця функція повинна приймати на вхід рядок і повертати кількість
 голосних (a, e, i, o, u) у рядку. Функція повинна бути нечутливою до регістру.
"""


def count_vowels(text: str) -> int:
    vowels = "aeiou"
    sum = 0
    for char in text.lower():
        if char in vowels:
            sum += 1
    return sum


print(count_vowels("Hello"))

# print("_________________________________")

"""Обчислити суму цілих чисел від 1 до заданого N (включно).
"""


def sum_upto_n(N: int) -> int:
    sum = 0
    for i in range(N + 1):
        sum += i
    return sum


print(sum_upto_n(2))

assert sum_upto_n(1) == 1
assert sum_upto_n(2) == 3
assert sum_upto_n(3) == 6
assert sum_upto_n(4) == 10
print("_________________________________")

"""
Ваша функція повинна отримати на вхід рядок і перетворити
всі перші літери слів у рядку у верхній регістр, 
зробивши рядок заголовним (інші літери повинні бути у нижньому регістрі).
"""


def to_title_case(sentence: str) -> str:
    return sentence.title()


print("Example:")
print(to_title_case("hello world"))

# These "asserts" are used for self-checking
assert to_title_case("hello world") == "Hello World"
assert to_title_case("openai gpt-4") == "Openai Gpt-4"
assert to_title_case("this is a title") == "This Is A Title"
assert to_title_case("THE QUICK BROWN FOX") == "The Quick Brown Fox"
assert to_title_case("JUMPs ovER a LAZy dog") == "Jumps Over A Lazy Dog"
assert to_title_case("typescript is great") == "Typescript Is Great"
assert to_title_case("the answer is 42") == "The Answer Is 42"
assert to_title_case("to be or not to be") == "To Be Or Not To Be"
assert to_title_case("that is the question") == "That Is The Question"
assert to_title_case("") == ""

print("_________________________________")
"""
Ця функція повинна приймати на вхід три рядки: 
    основний текст, 
    шуканий підрядок 
    і підрядок-замінник. 
Вона повинна повернути новий рядок, 
у якому всі входження цільового підрядка 
в основному тексті замінено на підрядок-замінник.
"""


def replace_all(mainText: str, target: str, repl: str) -> str:
    return mainText.replace(target, repl)


print(replace_all("hello world", "world", "TypeScript"))

# These "asserts" are used for self-checking
assert replace_all("hello world", "world", "TypeScript") == "hello TypeScript"
assert (
        replace_all("hello world world", "world", "TypeScript")
        == "hello TypeScript TypeScript"
)
assert replace_all("TypeScript is fun", "fun", "awesome") == "TypeScript is awesome"
assert replace_all("aaa", "a", "b") == "bbb"
assert replace_all("replace all the all", "all", "some") == "replace some the some"
assert replace_all("nothing to replace", "something", "nothing") == "nothing to replace"
assert replace_all("same same same", "same", "same") == "same same same"

print("_________________________________")

"""Ця функція повинна приймати на вхід ціле невід'ємне число 
і повертати факторіал цього числа. 
Факторіал невід'ємного числа n - це добуток усіх натуральних чисел, 
менших або рівних n."""


def factorial(n: int) -> int:
    res = 1
    if n == 0:
        return res
    for i in range(n):
        res *= i + 1
    return res


print(factorial(1))

# These "asserts" are used for self-checking
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800
assert factorial(15) == 1307674368000
print("_________________________________")

"""Тобі дано рядок і два маркери (початковий маркер та кінцевий маркер).
Тобі потрібно знайти текст, який заключений у ці два маркера.
Але є декілька важливих умов.

Початковий та кінцевий маркери завжди різні.
Початковий та кінцевий маркери завжди розміром в один символ.
Початковий та кінцевий маркери завжди є в рядку і ідуть один за другим.
"""


def between_markers(text: str, start: str, end: str) -> str:
    # Знаходимо індекси маркерів
    start_index = text.index(start) + 1
    end_index = text.index(end, start_index)
    # Повертаємо текст між маркерами
    return text[start_index:end_index]


print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"
print("_________________________________")

"""У заданому рядку потрібно перевірити, чи один символ йде відразу за іншим. 
Якщо так - повернути True, інакше - False.
Якщо один із символів відсутній у слові - твоя функція повинна повертати False. 
Якщо шукані символи однакові - твоя функція також повинна повертати False.
"""


def goes_after(word: str, first: str, second: str) -> bool:
    n = len(word)
    for i in range(n - 1):
        if i < n and first == word[i] and second == word[i + 1]:
            return True
    return False


print(goes_after("world", "w", "o"))

assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

print("_________________________________")

"""Функція повинна повернути найбільшу цифру у числі.
"""


def max_digit(value: int) -> int:
    max = value % 10
    value = value // 10
    while value > 0:
        if value % 10 > max:
            max = value % 10
        value //= 10
    return max


print(max_digit(150))

# These "asserts" are used for self-checking
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1
print("_________________________________")

"""
У заданому тексті тобі потрібно підсумувати числа, 
виключивши будь-які цифри, які є частиною слова.
"""


def sum_numbers(text: str) -> int:
    l = text.split()
    sum = 0
    for item in l:
        if item.isnumeric():
            sum += int(item)
    return sum


print(sum_numbers("hi"))

# These "asserts" are used for self-checking
assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
        sum_numbers(
            "This picture is an oil on canvas painting by Danish artist "
            "Anna Petersen between 1845 and 1910 year"
        )
        == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0
print("_________________________________")

"""Заданий рядок зі словами і числами, розділеними пробілами 
(один пробіл між словами та / або числами). Слова складаються 
тільки з букв. Вам потрібно перевірити чи є у вихідному рядку 
три слова підряд. 
Наприклад, в рядку "start 5 one two three 7 end" є три слова підряд.
"""


def checkio(words: str) -> bool:
    l = words.split()
    count = 0
    for item in l:
        if not item.isnumeric():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False


print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("_________________________________")
"""Вхідний рядок складається лише з цифр. 
Функція повинна повернути кількість нулів від початку рядка."""


def beginning_zeros(a: str) -> int:
    # str_length = len(a)
    # num = int(a)
    # if num==0:
    #     return str_length
    # else:
    #     return str_length - len(str(num))

    # или
    return len(a) - len(a.lstrip('0'))


print(beginning_zeros("0000"))

# These "asserts" are used for self-checking
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
assert beginning_zeros("012345679") == 1
assert beginning_zeros("0000") == 4

a = "001001"
print(a.lstrip('0'))  # 1001
b = "00100100"
print(b.rstrip('0'))  # 001001

print("_________________________________")

"""
Ця функція повинна приймати на вхід рядок без розділових 
знаків і повертати найдовше слово у рядку. 
Якщо у рядку є декілька слів однакової довжини, 
поверніть перше, яке з'явиться на екрані.
"""


def longest_word(sentence: str) -> str:
    words = sentence.split()
    if not words:
        return ""
    res = max(words, key=len)
    return res


print(longest_word("hello world"))

# These "asserts" are used for self-checking
assert longest_word("hello world") == "hello"
assert longest_word("openai gpt-4") == "openai"
assert longest_word("this is a sentence") == "sentence"
assert longest_word("the quick brown fox") == "quick"
assert longest_word("jumped over the lazy dog") == "jumped"
assert longest_word("typescript is great") == "typescript"
assert longest_word("the answer is 42") == "answer"
assert longest_word("to be or not to be") == "not"
assert longest_word("that is the question") == "question"
assert longest_word("") == ""
assert longest_word(" ") == ""
print("_________________________________")


def max_of_three(a: int, b: int, c: int) -> int:
    return max(a, max(b, c))


def max(a, b):
    if a > b:
        return a
    return b


print("_________________________________")
""""Можливо, я вже бачив спрощену версію цієї місії First Word (simplified). Ця місія трохи складніша, оскільки в заданому рядку можуть бути не лише англійські літери.

Тобі дається рядок, в якому ти повинен знайти його перше слово.

При розв’язуванні задачі зверни увагу на такі моменти:

У рядку можуть бути крапки і коми.
Рядок може починатися з літери або, наприклад, однієї/кількох крапок або пробілів.
Слово може містити апостроф, він являється частиною слова.
Весь текст можна представити одним словом і все."""

name = ""
name2 = "    stas../,,"
name3 = "don't"
print(name3.isalpha())

import re


def first_word(text):
    # Используем регулярное выражение для поиска первого слова,
    # включая апострофы
    match = re.search(r"[a-zA-Z']+", text)
    if match:
        return match.group(0)
    return ""


print(first_word("... and so on ..."))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"

print("_________________________________")
"""
За заданими двома рядками і допустимою кількістю 
відмінностей символів визначте, 
чи можна вважати ці рядки приблизно рівними."""


def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    if threshold == 0:
        return False
    count = 0
    for a, b in zip(str1, str2):
        if a == b:
            count += 1
    if count >= threshold:
        return True
    else:
        return False


print(fuzzy_string_match("apple", "appel", 2))

# These "asserts" are used for self-checking
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False

print("_________________________________")
"""Досконале число - це натуральне число, 
яке дорівнює сумі своїх правильних дільників, за винятком самого себе. 
 Наприклад, 28 є досконалим числом, оскільки його дільниками 
 є 1, 2, 4, 7 і 14, а їх сума дорівнює 28.
 """

def is_perfect(n: int) -> bool:
    numbers=[]
    for i in range(1, n-1):
        if n % i==0:
           numbers.append(i)
    print(numbers)
    res = sum(numbers)
    print(res)
    if res==n:
        return True
    else:
        return False


#or
def is_perfect2(n: int) -> bool:
    res = sum (i for i in range(1, n-1) if n % i==0)
    return res == n


print("Example:")
print(is_perfect2(6))

# These "asserts" are used for self-checking
assert is_perfect(6) == True
assert is_perfect(2) == False
assert is_perfect(28) == True
assert is_perfect(20) == False
assert is_perfect(496) == True
assert is_perfect(30) == False
assert is_perfect(8128) == True
assert is_perfect(100) == False
assert is_perfect(500) == False
assert is_perfect(1000) == False
