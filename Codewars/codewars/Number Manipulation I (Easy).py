"""

For a given large number (num),
write a function which returns
the number with the second half of digit
s changed to 0.

In cases where the number has an odd number of digits,
the middle digit onwards should be changed to 0."""
from os.path import split


# def manipulate(n):
#     s=''
#     l=[]
#     for c in str(n):
#         l.append(c)
#     length = len(l)//2
#     for i in range(length, len(l)):
#         l[i]="0"
#     for el in l:
#         s +=el
#     return int(s)

def manipulate(n):
    n = str(n)
    middle = len(n) // 2
    res  = n[:middle] + '0' * len(n[middle:])
    return int(res)

n = 192827764920
print(manipulate(n))  # 192827000000

name = "stanislav"
print(name[:5])