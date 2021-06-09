# -------------- Fibonnaci --------------
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


def fibonacci_iterative(num):
    """
    should return the nth value in the fibonacci series
    """
    if type(num) != int or num < 0:
        return None
    if num == 0:
        return 0
    if num == 1:
        return 1

    prev = 0
    current = 1
    up_next = 0
    count = num - 2

    while count >= 0:
        up_next = prev + current
        prev = current
        current = up_next
        count -= 1

    return up_next


# --------------- Lucas ---------------


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


def lucas_iterative(num):
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

    prev = 2
    current = 1
    up_next = 0
    count = num - 2

    while count >= 0:
        up_next = prev + current
        prev = current
        current = up_next
        count -= 1

    return up_next


# -------------- Sum_Series --------------


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

    return sum_series_recursive(num - 1, a, b) + sum_series_recursive(num - 2, a, b)


def sum_series_iterative(num, a=0, b=1):
    if type(num) != int or num < 0:
        return None
    if num == 0:
        return a
    if num == 1:
        return b

    prev = a
    current = b
    up_next = 0
    count = num - 2

    while count >= 0:
        up_next = prev + current
        prev = current
        current = up_next
        count -= 1

    return up_next


if __name__ == "__main__":

    # print("--------fibonacci_recursive----------")
    # for i in range(12):
    #     print(fibonacci_recursive(i))

    # print("--------fibonacci_iterative----------")
    # for i in range(12):
    #     print(fibonacci_iterative(i))

    # print("--------lucas_recursive----------")
    # for i in range(12):
    #     print(lucas_recursive(i))

    # print("--------lucas_iterative----------")
    # for i in range(12):
    #     print(lucas_iterative(i))

    # print("--------sum_series_recursive--2--1------")
    # for i in range(12):
    #     print(sum_series_recursive(i, 5, 3))

    # print("--------sum_series_iterative--2--1------")
    # for i in range(12):
    #     print(sum_series_iterative(i, 5, 3))

    pass
