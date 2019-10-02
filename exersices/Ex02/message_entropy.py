""" MESSAGE ENTROPY """
from math import log


def letter_freq(txt):

    txt_lower = txt.lower()
    """Removes caps from all letters."""

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', ' ', '!', '?', ',',
                '.', '+', '-', '_', '&', '%', '(', ')', '"', ':']

    txt_dictionary = {}

    for i in range(len(alphabet)):
        if txt_lower.count(alphabet[i]) != 0:
            txt_dictionary[ord(alphabet[i])] = txt_lower.count(alphabet[i])
    """Fills a dictionary with all letters, however instead of storing each
     letter and its corresponding frequency, we store its utf8-value instead 
     of the letter."""

    return txt_dictionary


def entropy(message):
    """Function entropy calculates the total entropy in the input"""

    letter_frequencies = letter_freq(message)
    """Calls on a function letter_frequencies which outputs a 
        dictionary with the key: utf8-value og the letters in input 
        message and value: time the utf8-value occurs in input."""

    repeated_letter = letter_frequencies.values()
    """Counts how many times the utf8-values occur in the input"""

    number_of_letters = len(message)
    """Total number of letters in input"""

    entropi = 0

    for index in range(len(letter_frequencies)):
        p_i = float(repeated_letter[index])/number_of_letters

        entropi += - p_i*log(p_i, 2)
    """calculates the fraction p_i which is defined as 
        repeated_letter/number of letters and uses it to find 
        the entropy in the input message"""

    return entropi


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
