poem = """
Свинки замяукали:
- Мяу, мяу!
Кошечки захрюкали:
- Хрю, хрю, хрю!
Уточки заквакали:
- Ква, ква, ква!
Курочки закрякали:
- Кря, кря, кря!
Воробышек прискакал
И коровой замычал:
- Мууу!
"""

def parse_poem(poem):
    res = {}
    lst = poem.strip().split('\n')
    animal= None
    for item in lst:
        if animal is None:
            animal = item.split()[0]
        elif item.startswith('-'):
            word = item.replace('-','').replace(' ','').replace("!",'').split(',')[0]
            res[animal] = word
            animal = None
    return res

print(parse_poem(poem))



parse_poem(poem)

