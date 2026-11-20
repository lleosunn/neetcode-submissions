class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # push numbers on the stack that haven't been used
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif t == "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif t == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(t)
        return stack[0]