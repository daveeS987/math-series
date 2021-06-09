def fibonacci_recursive(num):
    """
    should return the nth value in the fibonacci series
    """

    if type(num) != int or num < 0:
        return None
    if num == 0:
        return 0
    if num == 1:
        return 1

    return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)


def lucas_recursive(num):
    """
    should return the nth value in the lucas series
    lucas series starts with 2, 1
    """
    if type(num) != int or num < 0:
        return None
    if num == 0:
        return 2
    if num == 1:
        return 1

    return lucas_recursive(num - 1) + lucas_recursive(num - 2)


def sum_series_recursive(num, a=0, b=1):
    """
    should return the nth value in the series
    the series will start with a and second number will be b
    if no arguments are given, it will default to start with 0 and 1(Fibonacci)
    """
    if type(num) != int or num < 0:
        return None
    if num == 0:
        return a
    if num == 1:
        return b

    return sum_series_recursive(num - 1) + sum_series_recursive(num - 2)


# def fibonacci_iterative(num):
#     """
#     should return the nth value in the fibonacci series
#     """
#     pass


# def lucas_iterative(num):
#     """
#     should return the nth value in the lucas series
#     lucas series starts with 2, 1
#     """
#     pass


# def sum_series_iterative(num, a=0, b=1):
#     pass
