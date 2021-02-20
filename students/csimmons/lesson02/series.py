#!/usr/bin/env python3
# Craig Simmons
# Python 210
# series.py - Lesson02 - Fibonacci Exercises
# Created 11/13/2020 - csimmons
# Modified 11/14/2020 - csimmmons

def sum_series(n,first=0,second=1):
    """ Compute the nth value of a summation series.

    :param first=0: value of zeroth element in the series
    :param second=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).

    sum_series(n, 3, 2) should generate another series with no specific name

    The defaults are set to 0, 1, so if you don't pass in any values, you'll
    get the fibonacci sercies
    """

    if n == 0:
        return(first)
    elif n == 1:
        return(second)
    else:
        return sum_series(n-2,first,second) + sum_series(n-1,first,second)
    pass

def fibonacci(n):
    """ Compute the nth Fibonacci number """
    return sum_series(n)
    pass

def lucas(n):
    """ Compute the nth Lucas number """
    return sum_series(n,2,1)
    pass

if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)
    assert sum_series(7, 2, 1) == lucas(7)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("All tests passed")