# 20. Valid Parentheses

def isValid(self, s: str) -> bool:

    if len(s) < 2:
        return False

    opened = ['(', '[', '{']
    closed = [')', ']', '}']
    
    stack = []
    
    for i in range(len(s)):
        if s[i] in opened:
            stack.append(s[i])
        elif s[i] in closed:
            if len(stack) == 0 or stack.pop() != opened[closed.index(s[i])]:
                return False
    
    if len(stack) > 0:
        return False
    return True