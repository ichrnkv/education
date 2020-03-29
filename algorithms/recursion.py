def matryoshka(n):
    """Prints matryoshka:)"""
    if n == 1:
        print('Matryoshka')
    else:
        print('Matryoshka top n={}'.format(n))
        matryoshka(n-1)
        print('Matryoshka bottom n={}'.format(n))


if __name__ == '__main__':
    matryoshka(5)
