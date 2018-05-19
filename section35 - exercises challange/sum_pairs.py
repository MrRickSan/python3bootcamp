'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''


def sum_pairs(my_list, num):
    counter = 0
    for i in my_list:
        counter += 1
        for j in my_list[counter:]:
            if i + j == num:
                return [i, j]
    return []


print(sum_pairs([4, 2, 10, 5, 1], 6))
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))
