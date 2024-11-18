def isCors(ch_top_stac, ch_to_app):
    if ch_top_stac == '(' and ch_to_app == ')':
        return True
    if ch_top_stac == '[' and ch_to_app == ']':
        return True
    if ch_top_stac == '{' and ch_to_app == '}':
        return True
    return False

def isValid(s):
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if stack and isCors(stack[-1], c):
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(isValid("(())"))