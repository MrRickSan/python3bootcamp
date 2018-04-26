from keyword import iskeyword


def contains_keyword(*args):
    for x in args:
      if iskeyword(x) == True: return True  
    return False

print(contains_keyword('rick', 'test'))
print(contains_keyword('rick', 'test', 'def'))