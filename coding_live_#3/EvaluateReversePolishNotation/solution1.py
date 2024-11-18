def evalRPN(tokens):
    stack = []
    for n in tokens:
        if n in {"+", "-", "*", "/"}:
            op1 = int(stack.pop())
            op2 = int(stack.pop())
            if n == "+":
                r = str(op1 + op2)
            elif n == "-":
                r = str(op2 - op1)
            elif n == "*":
                r = str(op1 * op2)
            elif n == "/":
                r = str(int(op2 / op1))
            stack.append(r)
        else:
            stack.append(n)
    return int(stack[0])

print(evalRPN(["4","13","5","/","+"]))