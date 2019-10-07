# Coding=utf-8

__author__ = 'Andreas Sandvik Hoeimyr'
__email__ = 'andrehoi@nmbu.no'


def bubble_sort(data):
    sorted_data = list(data)
    """The input data is a tuple, thus we need to convert it to a list."""

    n = len(data)
    while True:
        if n <= 0:
            break
        else:
            sorted_data = sorting_one_element(sorted_data)
        n -= 1
    """ An infinite loop which breaks if the parameter n is equal to zero. 
    n starts out equal to the length of the input tuple and is reduced by 1
     for each loop."""

    return sorted_data


def sorting_one_element(sorted_data):

    for index in range(len(sorted_data) - 1):
        if sorted_data[index] > sorted_data[index + 1]:
            sorted_data[index], sorted_data[index + 1] = \
                sorted_data[index + 1], sorted_data[index]
    """ A loop which checks if one element in the list is bigger than the one 
    to its right. If it is the two number swap place. 
    This is repeated until the element is in the correct 
    sorted place"""

    return sorted_data


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == [], 'List should be empty'


test_empty()


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([6]) == [6], 'List should contain 1 number'


test_single()


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    assert not bubble_sort([1, 3, 2]) == [1, 3, 2], 'Function does not ' \
                                                    'return an sorted list'


test_sorted_is_not_original()


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data == [3, 2, 1], 'function changed the input list'
    assert not data == sorted_data, 'function should not be equal to output'


test_original_unchanged()


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    sorted_data = bubble_sort([3, 2, 1])
    assert sorted_data == bubble_sort(sorted_data), 'Function bubble_sort' \
                                                    'does not work on' \
                                                    'already sorted lists'


test_sort_sorted()


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    assert bubble_sort([3, 2, 1]) == [1, 2, 3], 'Function does not sort ' \
                                                'revers-sorted lists'


test_sort_reversed()


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    assert bubble_sort([6, 6, 6]) == [6, 6, 6], 'function bubble_sort does' \
                                                'not work on lists with all' \
                                                'identical elements'


test_sort_all_equal()


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    assert bubble_sort([4, 3, 2, 1, 10]) == [1, 2, 3, 4, 10], \
        'Function does not take lists of this length'

    assert bubble_sort(['c', 'b', 'a']) == ['a', 'b', 'c'], 'function does' \
                                                            'not sort string'


test_sorting()
