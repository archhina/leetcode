# 150. Evaluate Reverse Polish Notation

def evalRPN(self, tokens: List[str]) -> int:

    if len(tokens) < 2:
        return int(tokens[0])
    
    stack = []

    total = 0

    for i, v in enumerate(tokens):
        if v in "+-*/":
            v2 = int(stack.pop())
            v1 = int(stack.pop())
            print(v1, v, v2)
            if v == "+":
                total = v1 + v2
            elif v == "-":
                total = v1 - v2
            elif v == "*":
                total = v1 * v2
            elif v == "/":
                total = int(v1 / v2)
            stack.append(total)
        else:
            stack.append(v)

    return total