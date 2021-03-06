'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''


def truncate(string, value):
    if value < 3:
        return 'Truncation must be at least 3 characters.'
    elif len(string) < value:
        return string
    return string[0:value - 3] + '...'


print(truncate("Super cool", 2))
print(truncate("Super cool", 1))
print(truncate("Super cool", 0))
print(truncate("Hello World", 6))
print(truncate("Problem solving is the best!", 10))
print(truncate("Yo", 100))
print(truncate("Another test", 12))
