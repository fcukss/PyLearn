from collections import Counter

def find_uniq(a):
    return Counter(a).most_common()[1][0]



print(find_uniq([2, 1, 1, 1, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))

assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
assert find_uniq([ 3, 10, 3, 3, 3 ]) == 10