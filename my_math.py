
def dgkim(a, b):
    """
    returns dgkim way of adding

    >>> dgkim(2, 3)
    4
    >>> dgkim(3, 4)
    9
    """
    return a + b + 1


if __name__=='__main__':
    import doctest, my_math
    doctest.testmod(my_math)

