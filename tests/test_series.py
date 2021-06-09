from math_series.series import fibonacci_recursive
from math_series.series import lucas_recursive
from math_series.series import sum_series_recursive

# from math_series.series import fibonacci_iterative
# from math_series.series import lucas_iterative
# from math_series.series import sum_series_iterative


# ---------------------- Fibonnaci ----------------------
def test_fibonacci_recursive_should_return_first_element():
    actual = fibonacci_recursive(0)
    expected = 0
    assert actual == expected


def test_fibonacci_recursive_should_return_second_element():
    actual = fibonacci_recursive(1)
    expected = 1
    assert actual == expected


def test_fibonacci_recursive_should_return_third_element():
    actual = fibonacci_recursive(2)
    expected = 1
    assert actual == expected


def test_fibonacci_recursive_should_return_tenth_element():
    actual = fibonacci_recursive(10)
    expected = 1
    assert actual == expected


def test_fibonacci_recursive_should_return_none_for_negative_numbers():
    actual = fibonacci_recursive(-5)
    expected = None
    assert actual == expected


def test_fibonacci_recursive_should_return_none_for_type_string():
    actual = fibonacci_recursive("im a string")
    expected = None
    assert actual == expected


def test_fibonacci_recursive_should_return_none_for_type_list():
    actual = fibonacci_recursive(["a", "b", "c"])
    expected = None
    assert actual == expected


def test_fibonacci_recursive_should_return_none_for_type_dictionary():
    actual = fibonacci_recursive({"a": "a string", "b": "another string"})
    expected = None
    assert actual == expected


# ---------------------- Lucas ----------------------


def test_lucas_recursive_should_return_first_element():
    actual = lucas_recursive(0)
    expected = 2
    assert actual == expected


def test_lucas_recursive_should_return_second_element():
    actual = lucas_recursive(1)
    expected = 1
    assert actual == expected


def test_lucas_recursive_should_return_third_element():
    actual = lucas_recursive(2)
    expected = 3
    assert actual == expected


def test_lucas_recursive_should_return_tenth_element():
    actual = lucas_recursive(10)
    expected = 1
    assert actual == expected


def test_lucas_recursive_should_return_none_for_negative_numbers():
    actual = lucas_recursive(-5)
    expected = None
    assert actual == expected


def test_lucas_recursive_should_return_none_for_type_string():
    actual = lucas_recursive("im a string")
    expected = None
    assert actual == expected


def test_lucas_recursive_should_return_none_for_type_list():
    actual = lucas_recursive(["a", "b", "c"])
    expected = None
    assert actual == expected


def test_lucas_recursive_should_return_none_for_type_dictionary():
    actual = lucas_recursive({"a": "a string", "b": "another string"})
    expected = None
    assert actual == expected


# ---------------------- sum_series ----------------------


def test_sum_series_recursive_should_return_first_element():
    actual = sum_series_recursive(0)
    expected = 0
    assert actual == expected


def test_sum_series_recursive_should_return_second_element():
    actual = sum_series_recursive(1)
    expected = 1
    assert actual == expected


def test_sum_series_recursive_should_return_third_element():
    actual = sum_series_recursive(2)
    expected = 1
    assert actual == expected


def test_sum_series_recursive_should_return_tenth_element():
    actual = sum_series_recursive(10)
    expected = 1
    assert actual == expected


def test_sum_series_recursive_should_return_none_for_negative_numbers():
    actual = sum_series_recursive(-5)
    expected = None
    assert actual == expected


def test_sum_series_recursive_should_return_none_for_type_string():
    actual = sum_series_recursive("im a string")
    expected = None
    assert actual == expected


def test_sum_series_recursive_should_return_none_for_type_list():
    actual = sum_series_recursive(["a", "b", "c"])
    expected = None
    assert actual == expected


def test_sum_series_recursive_should_return_none_for_type_dictionary():
    actual = sum_series_recursive({"a": "a string", "b": "another string"})
    expected = None
    assert actual == expected
