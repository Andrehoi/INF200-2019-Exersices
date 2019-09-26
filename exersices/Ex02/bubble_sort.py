"""Bubble sorting algorithm"""


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
    """ An infinite loop which breaks if the parameter n is equal to zero. n starts out equal to the 
    length of the input tuple and is reduced by 1 for each loop."""

    return tuple(sorted_data)


def sorting_one_element(sorted_data):

    for index in range(len(sorted_data) - 1):
        if sorted_data[index] > sorted_data[index + 1]:
            sorted_data[index], sorted_data[index + 1] = sorted_data[index + 1], sorted_data[index]
    """ A loop which checks if one element in the list is bigger than the one to its right. 
    If it is the two number swap place. This is repeated until the element is in the correct 
    sorted place"""

    return sorted_data


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
