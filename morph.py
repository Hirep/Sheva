"""This module contains tools for our morphological analyzer.
"""

class Word:
    """This class stores info about word
        __init__(
            str     word    # is a word itself
            int     id      # gets id from root dict
            str     begin   # beginning of the word (word-ending)
            str     ending  # ending of the word
        )
    """
    def __init__(self, word, id, begin, ending):
        self.word = word
        self.id = id
        self.begin = begin
        self.ending = ending
        self.role = None
        self.syntax_role = None
        
    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.word, self.id, self.ending, self.role, self.syntax_role)


def get_word_ending(word):
    """ str word    # word to take ending from
        returns str ending  # just what's left after taking out word root found in dict
    """
    return word[len(beg):]