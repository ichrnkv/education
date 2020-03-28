def insert_sort(A):
    """ Insert sorting """
    n = len(A)
    for top in range(1, n):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1


def choise_sort(A):
    """ Sorting by choice """
    n = len(A)
    for pos in range(0, n-1):
        for k in range(pos+1, n):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    """ Bubble sort """
    n = len(A)
    for bypass in range(1, n):
        for k in range(0, n-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]



def test_sort(sort_algorithm):
    print('Test of: {}'.format(sort_algorithm.__doc__))
    print('#test1: ', end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Failed')

    print('#test2: ', end='')
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Failed')

    print('#test3: ', end='')
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Failed')


if __name__ == '__main__':
    for algorithm in [insert_sort, choise_sort, bubble_sort]:
        test_sort(algorithm)
