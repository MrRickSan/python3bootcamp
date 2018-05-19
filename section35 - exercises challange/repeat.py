'''
repeat('*', 3) # '***'
repeat('abc', 2) # 'abcabc'
repeat('abc', 0) # ''
'''


def repeat(string, times):
    # return string * times

    # or without python built-in repeat
    if times == 0:
        return ''
    result = string
    for n in range(1, times):
        result += string
    return result


print(repeat('*', 3))
print(repeat('abc', 2))
print(repeat('abc', 0))
