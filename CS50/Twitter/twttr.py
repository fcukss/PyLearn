def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    res=''
    pattern = "AEIOUaeiou"
    for c in word:
        if c in pattern:
            continue
        else:
            res+=c
    return res

if __name__ == '__main__':
    main()