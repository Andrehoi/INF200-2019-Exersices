# Coding=utf-8

__author__ = 'Andreas Sandvik Hoeimyr'
__email__ = 'andrehoi@nmbu.no'

"""Source: https://github.com/yngvem/
INF200-2019-Exercises/blob/master/exersices/ex03.rst"""

"""Median of a list of numbers"""


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """
    if len(data) < 1:
        raise ValueError

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
            else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


def test_one_element():
    """Tests if function median returns the correct value if only one element
    in the input."""

    assert median([5]) == 5, 'Function median does not handle one-element' \
                             'inputs correctly!'


def test_correct_median():
    """ Checks if the correct median is returned for lists with odd number
    of elements, even number of elements and lists with different orders of
    numbers e.g. sorted, revers-sorted and unordered."""

    assert median([1, 3, 1, 3]) == 2, 'Function returns wrong median for ' \
                                      'lists with even number of elements'

    assert median([1, 2, 3]) == 2, 'Function returns wrong median for ' \
                                   'lists with odd number of elements'

    assert median([3, 2, 1]) == 2, 'Function returns wrong median for ' \
                                   'revers-ordered lists'

    assert median([5, 1, 3, 4, 2, 3]) == 3, 'Function returns wrong median ' \
                                            'for unordered lists'


test_correct_median()


def test_empty_list():
    """Tests if the function gives a ValueError if it is given
    an empty list."""

    try:
        median([])

    except ValueError:
        pass

    else:
        assert False


test_empty_list()


def test_unchanged_input_data():
    """Tests if the function alters the input data."""

    data = [1, 2, 3, 5, 4]

    median_data = median(data)

    assert data == [1, 2, 3, 5, 4]

    assert median_data == median([1, 2, 3, 5, 4])


test_unchanged_input_data()


def test_median_of_tuples():
    """Tests if the function can handle if the input data is a tuple"""

    assert median((1, 2, 3)) == 2, 'function median can not handle tuples'


test_median_of_tuples()
