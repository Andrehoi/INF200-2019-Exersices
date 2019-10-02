"""File stats"""


def char_counts(textfilename):
    """Char_counts is a function which opens the input file.
    It then converts the file into a single string. Then it converts the
    letters into utf8 values and outputs the number of times the utf8-values
     are repeated """

    text_string = open(textfilename).read()
    """ Converts the file into a string"""

    character_list = [characters.split() for characters in text_string]
    """ Makes a list of lists of the string"""

    character_list2 = [x for x in character_list if x]
    print(character_list2)
    """ Removes all spaces from character_list, thus only elements with
     utf8-values are left in the list"""

    utf8_value = []
    for i in range(len(character_list2)):
        utf8_value.append(ord(character_list2[i][0]))
    """ Creates a list of the utf8-values of the letters in character_list2.
         By indexing we can remove the '' surrounding each letter."""

    results = [utf8_value.count(key) for key in range(len(utf8_value))]
    """ Creates the requested list with the number of repeated utf8-values. """

    return results


if __name__ == '__main__':

    filename = 'file_stats.py'

    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
