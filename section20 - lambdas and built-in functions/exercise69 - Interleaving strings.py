# my answer
def interleave(string1, string2):
    return "".join(list(
                        map(
			             lambda pair: ((pair[0]+pair[1])),
			             zip(string1, string2)
		                )
                    )
                )

print(interleave('hi','no'))

# way 2 (his answer)
def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))