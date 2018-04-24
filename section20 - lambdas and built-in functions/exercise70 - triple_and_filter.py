'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(lst):
    return [x*3 for x in lst if x%4 == 0]

print(triple_and_filter([6,8,10,12]))

# solution 2
def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))
