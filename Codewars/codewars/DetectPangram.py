import string

def is_pangram(st):
    alphabet = set(string.ascii_lowercase)
    letters_in_st = set(st.lower())
    return alphabet.issubset(letters_in_st)