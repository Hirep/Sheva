import  parser_diagram

phrase = 'Кохайтеся чорнобриві, та не з москалями, бо москалі чужі люди, роблять лихо з вами.'

q1 = 'Що не потрібно робити з москалями?'
q2 = 'Чому не можна кохатися?'


# print(q2_transformed)

def get_answer(phrase, question):
    par, root_dict = parser_diagram.load_dict()

    q2_transformed, start, tt = parser_diagram.find_lang_part(question)
    phrase_trans, ph_st, tt2 = parser_diagram.find_lang_part(phrase)
    print("Phrase: {}".format(phrase))
    print("Question: {}".format(question))

    if start[0] == 'ОО':
        indexAns = ph_st.index('ОА')
        result = ''
        for i in range(len(phrase_trans)):
            if i >= indexAns:
                result += phrase_trans[i] + ' '

        result2 = result[0].upper() + result[1:]
        print("Answer: {}".format(result2))
    elif start[0] == 'ОР': # коха + тися  рут + ДД
        # indexAns = par[1]
        # print(indexAns)


        # result2 = root_dict[indexAns]
        result2 = 'Кохатися'
        print("Answer: {}".format(result2))




get_answer(phrase,q1)