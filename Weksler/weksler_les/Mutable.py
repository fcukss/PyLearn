#
# def add_to_grocery_list(grocery_list=[], grocery=""):
#     grocery_list.append(grocery)
#     print(grocery_list)

# # вызывается одна и таже функция но вывод разный.
# add_to_grocery_list(grocery="trava")  #['trava']
# add_to_grocery_list(grocery="U doma")  #['trava', 'U doma']
"""

НИКОГДА НЕ ИСПОЛЬЗОВАТЬ ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ MUTTABLE(ИЗМЕНЯЕМЫЕ ТИП)
"""
class Entry:
    #так делать не нужно потому что обькты класса Entry
        # будут ссылатся на один и тот же ИЗМЕНЯЕМЫЙ лист
    def __init__(self, title, entries = []):
        self.title = title
        self.entries = entries

entry = Entry("Test")
entry.entries.append('test')
entry.entries.append('passed')
print(entry.entries)   #['test', 'passed']


entry2 = Entry("test2")
print(entry2.entries)  #['test', 'passed']
entry2.entries.append('test2')
# два листа динаковые хотя обьекты разные, потому что ссылаются на один и тот же лист
print(entry2.entries)  #['test', 'passed', 'test2']
print(entry.entries)   #['test', 'passed', 'test2']

print("________________________")
class Entry2:
    #теперь будет создаваться новый лист
    def __init__(self, title, entries =None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries

entry = Entry2("Test")
entry.entries.append('test')
entry.entries.append('passed')
print(entry.entries)   #['test', 'passed']


entry2 = Entry2("test2")
print(entry2.entries)  #[]
entry2.entries.append('test2')
#два результатат разные
print(entry2.entries)  #['test2']
print(entry.entries)   #['test', 'passed']