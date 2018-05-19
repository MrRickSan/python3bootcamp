'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''


def titleize(string):
    list_of_strings = string.split(' ')
    result = []
    for string in list_of_strings:
        result.append(string[0].upper()+string[1:])
    return ' '.join(result)


print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))
