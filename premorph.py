"""This module contains tools for premorphological analysis.

"""


import regex as re

SENTENCES_RE = '[\.\!\?]+'
WORDS_RE = '[^[:alnum:]]+'
ENG_RE = u"[a-zA-Z]{2,}"
ABBR_RE = u"[\u0410-\u042F]{2,}"

def split_with_rexp(text, rsplt):
    sentences = re.split(rsplt, text.lower())
    return (
        sentences
        if sentences[-1] != ''
        else sentences[:-1]
    )


def split_by_sentences(text):
    return split_with_rexp(text, SENTENCES_RE)


def split_by_words(text):
    return filter(lambda x: bool(x), split_with_rexp(text, WORDS_RE))


def find_abbr(sentence):
    """
    :param sentence:
    :return:
    """
    abbr_list = re.findall(ABBR_RE, sentence)  # А-Я
    return abbr_list

def find_eng(sentence):
    """

    :param sentence:
    :return:
    """
    eng_list = re.findall(ENG_RE, ukr)  # А-Я
    return eng_list



def premorph(text):
    """ str text    # may be single sentence or whole text to analyze    
        returns iterator, yielding lists of words

        Main function in this module. Splits input text into sentences
        and sentences into words, generating input for next stage of analyzer.
    """
    return map(
        split_by_words,
        split_by_sentences(text)
    )