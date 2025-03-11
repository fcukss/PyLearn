def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    elif size <= 3:
        return phrase[:size] + '...'
    else:
        return phrase[:size - 3] + '...'


res = trim("Creating kata is fun", 14)
res = trim("Hey", 2)
res = trim("He", 1)
print(res)