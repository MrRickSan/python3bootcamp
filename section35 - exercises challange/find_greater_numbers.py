'''
find_greater_numbers([1,2,3]) # 3
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''


def find_greater_numbers(lista):
    counter = 0
    for index, row in enumerate(lista):
        counter += sum(1 for x in lista[index:] if x > row)
    return counter


print(find_greater_numbers([1, 2, 3]))
print(find_greater_numbers([6, 1, 2, 7]))
print(find_greater_numbers([5, 4, 3, 2, 1]))
