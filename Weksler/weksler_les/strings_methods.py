"""split - разделяет фразу, преобразуя в лист"""
from prompt_toolkit.search import start_search

phrase = '   hello, my name is Stas'
phrase.split()

#> ['hello,', 'my', 'name', 'is', 'Stas']

# можно указать какой именно разделитель использовать
phrase.split(',')
#> ['  hello', ' my name is Stas']


# Текст, состоящий из нескольких строк можно задать так (кавычки три раза):
text = """Съешь ещё этих мягких
французских булок,
да выпей чаю"""

print(text.split('\n'))
#['Съешь ещё этих мягких', 'французских булок,', 'да выпей чаю']

####################################################
"""strip - убирает символы по краям, например лишние пробелы"""
phrase = '   hello, my name is Stas'
print(phrase.strip())   #hello, my name is Stas

#############################
"""replace - заменяет слово/буквы в тексте"""

print(phrase.replace('Stas', 'Stas Kaplia'))  #   hello, my name is Stas Kaplia

"""startswith, endswith - проверяет, начинается/заканчивается ли переменная с какого-то текста"""
print(phrase.startswith('hello'))  #False

#убрали пробелы
print(phrase.strip().startswith('hello')) #True

