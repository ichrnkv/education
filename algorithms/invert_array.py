def invert_array(A):
    """
    Inverts array
    :param A: list
    :return:
    """
    n = len(A)
    for k in range(n//2):
        A[k], A[n-1-k] = A[n-1-k], A[k]


def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    invert_array(A1)
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print('#test1 passed')
    else:
        print('#test1 failed')

    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(A2)
    invert_array(A2)
    print(A2)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print('#test2 passed')
    else:
        print('#test2 failed')

if __name__ == '__main__':
    test_invert_array()
