'''
reverse_vowels("Hello!") # "Holle!"
reverse_vowels("Tomatoes") # "Temotaos"
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''


def reverse_vowels(string):
    vowels = list(filter(lambda x: x in 'aeiouAEIOU', string))[::-1]
    result = ""
    for i in string:
        if i in 'aeiouAEIOU':
            result += vowels.pop(0)
        else:
            result += i
    return result


print(reverse_vowels("Hello!"))
print(reverse_vowels("Reverse Vowels In A String"))
