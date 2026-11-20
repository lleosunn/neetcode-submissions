class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # push numbers on the stack that haven't been used
        stack = []
        for t in tokens:
            if t == "+":
                return stack.pop() + stack.pop()
            elif t == "-":
                b, a = stack.pop(), stack.pop()
                return a - b
            elif t == "*":
                return stack.pop * stack.pop()
            elif t == "/":
                b, a = stack.pop(), stack.pop()
                return int(a / b)
            else:
                stack.append(t)
        return stack[0]