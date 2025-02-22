def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

def reverse_words2(text):
    l = text.split(' ')
    for i in range(len(l)):
        l[i] = l[i][::-1]
    return ' '.join(l)

def reverse_each_word(s):
    result = []
    word = []
    for char in s:
        if char != ' ':
            word.append(char)
        else:
            if word:
                result.append(''.join(word[::-1]))
                word = []
            result.append(' ')
    if word:
        result.append(''.join(word[::-1]))
    return ''.join(result)

text = "  a b c d  "
print(reverse_words2(text))