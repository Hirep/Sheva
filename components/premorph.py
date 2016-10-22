"""This module contains tools for premorphological analysis.

"""


import regex as re

SENTENCES_RE = r"\[\.\!\?]\s*[A-ZА-Я]"
WORDS_RE = '[^[:alnum:]]+'
ENG_RE = u"[a-zA-Z]{2,}"
ABBR_RE = r"[\u0410-\u042F]{2,}"


SENTENCES_RE_NEW = u"""([А-Яа-яІієЄЇїҐґ][А-Яа-яІієЄЇїҐґ"»)]+)|[0-9])([.\?!]|…|...?|\?!|!\?|\?\?\??|!!!?)["»]? [А-ЯІЄЇҐ"«] )"""
WORDS_RE_NEW = u"""[А-Яа-яІієЄЇїҐґ']+"""
ENG_RE_NEW = u"""[A-Za-z]+"""
NUM_RE = u"""[0-9]+"""
ABBR_RE_NEW = u"""[А-ЯІЄЇҐ][А-ЯІЄЇҐ]+"""


def split_with_rexp(text, rsplt):
    sentences = [x.lower() for x in re.split(rsplt, text)]
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
    eng_list = re.findall(ENG_RE, sentence)  # А-Я
    return eng_list

#BAG BUG TODO
#print(find_abbr("віаівра ШОРЬРІОВ віаіватів іваьі тватівт івта ітват "))


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

