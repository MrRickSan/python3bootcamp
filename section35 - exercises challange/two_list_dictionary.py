'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': null}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': null}
'''


def two_list_dictionary(list1, list2):
    dict1 = {}.fromkeys(list1, None)  # dict 1 is a list1 dict with None values
    dict2 = dict(zip(list1, list2))
    return {**dict1, **dict2}  # merge two dictionaries


print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
