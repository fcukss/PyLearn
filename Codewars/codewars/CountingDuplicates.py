def duplicate_count(text):
    chars = []
    text = text.lower()
    for ch in text:
        if text.count(ch)>1:
            chars.append(ch)
    return len(set(chars))




print(duplicate_count('abcde'))




def test_duplicates():
    assert duplicate_count('abcde')==0
    assert duplicate_count('aabbcde') == 2
    assert duplicate_count('aabBcde') == 2
    assert duplicate_count('Indivisibilities') == 2
    assert duplicate_count('aA11') == 2