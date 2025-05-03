def largest(n, xs):
    new_arr = sorted(xs)
    if n==0:
        return []
    return new_arr[-n:]




print(largest(2, [7,6,5,4,3,2,1]))