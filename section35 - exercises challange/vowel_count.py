'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''


def vowel_count(string):
    string_as_list = list(string.lower())
    return {k: string_as_list.count(k) for k in string_as_list if k in ['a', 'e', 'i', 'o', 'u']}


print(vowel_count('awesome'))
print(vowel_count('Elie'))
print(vowel_count('Colt'))
