'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''


def list_check(arg1):
    for row in arg1:
        if type(row) != list:
            return False
    return True


print(list_check([[], [1], [2, 3], (1, 2)]))  # False
print(list_check([1, True, [], [1], [2, 3]]))  # False
print(list_check([[], [1], [2, 3]]))  # True
