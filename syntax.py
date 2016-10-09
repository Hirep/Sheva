import  parser_diagram




def cond1(word_role):
    list_roles = ['ПГ', 'ІЙ', 'ІЗ', 'ІШ', 'ІС', 'МЦ', 'МВ', 'ЛА', 'ПЙ']
    cond = [x == word_role for x in list_roles]
    for x in cond:
        if x:
            return True
    return False


def cond2(word_role):
    list_roles = ['ІЦ', 'ІУ', 'ІЕ', 'ІН', 'ІФ', 'ІВ', 'ІП', 'ІР', 'МК', 'МН', 'МП', 'МТ', 'ЛУ', 'ЛК', \
                  'ЛЕ', 'ЛН', 'ЛЗ', 'ЛД', 'ЛО', 'ЛР', 'ЛЦ', 'ЛЩ', 'ЛШ', 'ЗЕ']
    cond = [x == word_role for x in list_roles]
    for x in cond:
        if x:
            return True
    return False

def syntax(phrase1):

    k, l, words = parser_diagram.find_lang_part(phrase1)
    for word in words:
        if word.role == None:
            pass
        elif word.role[0] == 'Д' or word.role[0] == 'С':
            word.syntax_role = 'predicate'
        elif cond1(word.role):
            word.syntax_role = 'subject'
        elif word.role[0] == 'П' or word.role == 'КЛ':
            word.syntax_role = 'attribute'
        elif cond2(word.role):
            word.syntax_role = 'object'
        else:
            word.syntax_role = ''

    for word in words:
        print(word.word, word.syntax_role)

#TEST TODO

uk = 'Кохайтеся чорнобриві, та не з москалями. Москалі чужі люди, роблять лихо з вами.'

q2 = 'Чому не можна кохатися?'
print(syntax(q2))