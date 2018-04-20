nums = [x for x in range(1,10)]

double = map(lambda x: x*2, nums)

print(list(double))



#############################################

def decrement_list(my_list):
    return list(map(lambda x: x-1, my_list))

print(decrement_list(nums))