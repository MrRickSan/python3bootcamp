'''
includes([1, 2, 3], 1) # True
includes([1, 2, 3], 1, 2) # False
includes({ 'a': 1, 'b': 2 }, 1) # True
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''


def includes(collection, value, index=None):
    if type(collection) == list:
        if index:
            if value in collection[index:]:
                return True
        else:
            if value in collection:
                return True
        return False
    elif type(collection) == dict:
        if value in list(collection.values()):
            return True
        return False
    else:
        if value in collection:
            return True
        return False


print(includes([1, 2, 3], 1))
print(includes([1, 2, 3], 1, 2))
print(includes({'a': 1, 'b': 2}, 1))
print(includes({'a': 1, 'b': 2}, 'a'))
print(includes('abcd', 'b'))
print(includes('abcd', 'e'))
