'''
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
'''


def find_factors(num):
    factors = []
    for n in range(1, num + 1):
        if num % n == 0:
            factors.append(n)
    return factors


print(find_factors(10))  # [1,2,5,10 ]
print(find_factors(111))  # [1,3,37,111 ]
