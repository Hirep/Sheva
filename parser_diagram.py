import pandas as pd
import morph
import premorph


words_list = set()
errors_list = set()




def load_dict():
    """

    :return: par and root_dict
    """
    par = pd.read_excel('par_cls.xlsx', encoding='utf-8', header=None)
    par.columns = ['id', 'role', 'note', 'end']
    root_dict = pd.read_excel('root_dict.xlsx', encoding='utf-8', header=None)
    root_dict.columns = ['begin', 'end', 'id']

    return par, root_dict


def find_lang_part(text, ):

    #load data
    par, root_dict = load_dict()
    # Morpho
    words = []

    for i in premorph.premorph(phrase):
        for word in list(i):
            for beg in root_dict['begin']:
                if word.startswith(beg):
                    words.append(morph.Word(
                        word,
                        int(root_dict.loc[root_dict['begin'] == beg]['id']),
                        beg,
                        word[len(beg):] if len(word[len(beg):]) > 0 else ''
                    ))

    for word in words:
        for index, row in par.iterrows():
            if row['end'] == word.ending and row['id'] == word.id:
                word.role = row['role']
            elif (type(row['end']) is not str) and row['id'] == word.id and word.ending == '':
                word.role = row['role']

    for word in words:
        print(word.word, word.role)
    result_words = [word.word for word in words]
    result_roles = [word.roles for word in words]

    return result_words, result_roles

# phrase = 'Кохайтеся чорнобриві, та не з москалями. Москалі лихі люди, роблять лихо з вами.'
# find_lang_part(phrase)