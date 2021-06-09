from math_series.series import fibonacci_recursive
from math_series.series import lucas_recursive
from math_series.series import sum_series_recursive

from math_series.series import fibonacci_iterative
from math_series.series import lucas_iterative
from math_series.series import sum_series_iterative


# ---------------------- Fibonnaci Recursive ----------------------
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
    expected = 55
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


# ---------------------- Fibonnaci Iterative ----------------------
def test_fibonacci_iterative_should_return_first_element():
    actual = fibonacci_iterative(0)
    expected = 0
    assert actual == expected


def test_fibonacci_iterative_should_return_second_element():
    actual = fibonacci_iterative(1)
    expected = 1
    assert actual == expected


def test_fibonacci_iterative_should_return_third_element():
    actual = fibonacci_iterative(2)
    expected = 1
    assert actual == expected


def test_fibonacci_iterative_should_return_tenth_element():
    actual = fibonacci_iterative(10)
    expected = 55
    assert actual == expected


def test_fibonacci_iterative_should_return_none_for_negative_numbers():
    actual = fibonacci_iterative(-5)
    expected = None
    assert actual == expected


def test_fibonacci_iterative_should_return_none_for_type_string():
    actual = fibonacci_iterative("im a string")
    expected = None
    assert actual == expected


def test_fibonacci_iterative_should_return_none_for_type_list():
    actual = fibonacci_iterative(["a", "b", "c"])
    expected = None
    assert actual == expected


def test_fibonacci_iterative_should_return_none_for_type_dictionary():
    actual = fibonacci_iterative({"a": "a string", "b": "another string"})
    expected = None
    assert actual == expected


# ---------------------- Lucas Recursive ----------------------


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
    expected = 123
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


# ---------------------- Lucas Iterative ----------------------


def test_lucas_iterative_should_return_first_element():
    actual = lucas_iterative(0)
    expected = 2
    assert actual == expected


def test_lucas_iterative_should_return_second_element():
    actual = lucas_iterative(1)
    expected = 1
    assert actual == expected


def test_lucas_iterative_should_return_third_element():
    actual = lucas_iterative(2)
    expected = 3
    assert actual == expected


def test_lucas_iterative_should_return_tenth_element():
    actual = lucas_iterative(10)
    expected = 123
    assert actual == expected


def test_lucas_iterative_should_return_none_for_negative_numbers():
    actual = lucas_iterative(-5)
    expected = None
    assert actual == expected


def test_lucas_iterative_should_return_none_for_type_string():
    actual = lucas_iterative("im a string")
    expected = None
    assert actual == expected


def test_lucas_iterative_should_return_none_for_type_list():
    actual = lucas_iterative(["a", "b", "c"])
    expected = None
    assert actual == expected


def test_lucas_iterative_should_return_none_for_type_dictionary():
    actual = lucas_iterative({"a": "a string", "b": "another string"})
    expected = None
    assert actual == expected


# ---------------------- Sum_Series Recursive----------------------


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


def test_sum_series_recursive_should_return_twelfth_element():
    actual = sum_series_recursive(12)
    expected = 144
    assert actual == expected


def test_sum_series_recursive_should_return_first_element_if_input_2_1():
    actual = sum_series_recursive(0, 2, 1)
    expected = 2
    assert actual == expected


def test_sum_series_recursive_should_return_second_element_if_input_2_1():
    actual = sum_series_recursive(1, 2, 1)
    expected = 1
    assert actual == expected


def test_sum_series_recursive_should_return_third_element_if_input_2_1():
    actual = sum_series_recursive(2, 2, 1)
    expected = 3
    assert actual == expected


def test_sum_series_recursive_should_return_tenth_element_if_input_2_1():
    actual = sum_series_recursive(10, 2, 1)
    expected = 123
    assert actual == expected


def test_sum_series_recursive_should_return_none_for_negative_numbers():
    actual = sum_series_recursive(-5, 2, 1)
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


# ---------------------- Sum_Series Iterative----------------------


def test_sum_series_iterative_should_return_first_element():
    actual = sum_series_iterative(0)
    expected = 0
    assert actual == expected


def test_sum_series_iterative_should_return_second_element():
    actual = sum_series_iterative(1)
    expected = 1
    assert actual == expected


def test_sum_series_iterative_should_return_third_element():
    actual = sum_series_iterative(2)
    expected = 1
    assert actual == expected


def test_sum_series_iterative_should_return_twelfth_element():
    actual = sum_series_iterative(12)
    expected = 144
    assert actual == expected


def test_sum_series_iterative_should_return_first_element_if_input_2_1():
    actual = sum_series_iterative(0, 2, 1)
    expected = 2
    assert actual == expected


def test_sum_series_iterative_should_return_second_element_if_input_2_1():
    actual = sum_series_iterative(1, 2, 1)
    expected = 1
    assert actual == expected


def test_sum_series_iterative_should_return_third_element_if_input_2_1():
    actual = sum_series_iterative(2, 2, 1)
    expected = 3
    assert actual == expected


def test_sum_series_iterative_should_return_tenth_element_if_input_2_1():
    actual = sum_series_iterative(10, 2, 1)
    expected = 123
    assert actual == expected


def test_sum_series_iterative_should_return_none_for_negative_numbers():
    actual = sum_series_iterative(-5, 2, 1)
    expected = None
    assert actual == expected


def test_sum_series_iterative_should_return_none_for_type_string():
    actual = sum_series_iterative("im a string")
    expected = None
    assert actual == expected


def test_sum_series_iterative_should_return_none_for_type_list():
    actual = sum_series_iterative(["a", "b", "c"])
    expected = None
    assert actual == expected


def test_sum_series_iterative_should_return_none_for_type_dictionary():
    actual = sum_series_iterative({"a": "a string", "b": "another string"})
    expected = None
    assert actual == expected
