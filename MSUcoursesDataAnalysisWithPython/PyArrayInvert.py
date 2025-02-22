def invert_array(A:list, n:int):
    """поворот массива задом-наперед
    """
    for k in range(n//2):
        A[k],A[n-1-k]= A[n-1-k],A[k]


def test_invert_array():
    A1=[1,2,3,4,5]
    print(A1)
    invert_array(A1,5)
    print(A1)
    if A1==[5,4,3,2,1]:
        print("test1-ok")
    else:
        print("terst1-fail")

    A2 = [0,0,0,0,0,10]
    print(A2)
    invert_array(A2, 6)
    print(A2)
    if A2 == [10,0,0,0,0,0]:
        print("test2-ok")
    else:
        print("terst2-fail")

test_invert_array()