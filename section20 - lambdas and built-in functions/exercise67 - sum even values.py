'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''

# define sum_even_values

# way 1
def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)

#way 2
def sum_even_values(*args):
    lst = [x for x in args if x % 2 == 0]
    if lst:
        return sum(lst)
    return 0

print(sum_even_values(1,2,3,4,5,6))
print(sum_even_values(4,2,1,10))
print(sum_even_values(1))