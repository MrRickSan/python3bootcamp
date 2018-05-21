'''
valid_parentheses("()") # True
valid_parentheses(")(()))") # False
valid_parentheses("(") # False
valid_parentheses("(())((()())())") # True
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''


def valid_parentheses(parentheses_string):
    result = 0
    if parentheses_string[0] != '(':
        return False
    else:
        for char in parentheses_string:
            if char == '(':
                result += 1
            else:
                result -= 1
                if result < 0:
                    return False
    return result == 0


print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())"))
print(valid_parentheses('))(('))
print(valid_parentheses('())('))
