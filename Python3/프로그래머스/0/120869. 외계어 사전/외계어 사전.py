def solution(spell, dic):

    spell_sort_word = ''.join(sorted(spell))
    dic_sort = [''.join(sorted(w)) for w in dic]
    
    if spell_sort_word in dic_sort:
        answer = 1
    else:
        answer = 2
    
    return answer