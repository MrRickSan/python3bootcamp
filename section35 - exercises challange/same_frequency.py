'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''


def same_frequency(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))


print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
