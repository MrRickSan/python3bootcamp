'''
min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
'''


def min_max_key_in_dictionary(my_dict):
    lst = sorted(list(my_dict.keys()))
    return [lst[0], lst[-1]]


print(min_max_key_in_dictionary({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}))
print(min_max_key_in_dictionary({1: "Elie", 4: "Matt", 2: "Tim"}))
