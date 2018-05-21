'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''
# define mode below:


def mode(lst):
    bigger = 0
    for x in lst:
        if lst.count(x) > bigger:
            bigger = x
    return bigger


print(mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]))
