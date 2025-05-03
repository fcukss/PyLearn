def main():
    names=[]
    res = "Adieu, adieu, to "
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:  # Ctrl+D (конец ввода)
            break
    if len(names)==1:
        res+=names[0]
    elif len(names)==2:
        res+=names[0]+" and " + names[1]
    else:
        res+=', '.join(names[:-1])
        res+=', and ' + names[-1]
    return res




print(main())