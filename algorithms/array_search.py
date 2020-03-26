def array_search(A, x):
    """
    Brute force search for an item in the list.
    :param A: list
    :param x: required element
    :return: index of required element or -1 if element not in list
    """
    n = len(A)

    for idx in range(n):
        if A[idx] == x:
            return idx
    return -1


def test_array_search():
    """
    Prints results of simple tests of array_search function
    :return:
    """
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 8)
    if m == -1:
        print('# test1 passed')
    else:
        print('#test1 failed')

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, -3)
    if m == 2:
        print('# test2 passed')
    else:
        print('#test2 failed')

    A3 = [10, 3, 45, 99, 777777]
    m = array_search(A3, 10)
    if m == 0:
        print('# test3 passed')
    else:
        print('#test3 failed')


if __name__ == '__main__':
    test_array_search()
    print(array_search([1, 2, 3, 4, 5], 5))
