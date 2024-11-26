# using dict instead of helper function
def isValid(s):
    stack = []
    _map = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    for c in s :
        if c in _map.values():
            stack.append(c)
        else:
            if not stack or stack.pop() != _map[c] :
                return False
    return not stack

print(isValid("(())"))