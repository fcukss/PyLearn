def find_short(s):
    lst = s.split(' ')
    l = lst[0]
    for i in lst:
        if len(l) > len(i):
            l = i
    return len(l)  # l: shortest word length

print(find_short("bitcoin take over the world maybe who knows perhaps")) #->3