class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 3:
            tokens = self.calc[tokens[:3]] + tokens[3:]
        return calc(tokens)[0]
    
    def calc(self, exp):
        if exp[2] == "+":
            return [exp[0] + exp[1]]
        elif exp[2] == "-":
            return [exp[0] - exp[1]]
        elif exp[2] == "/":
            return [exp[0] / exp[1]]
        else:
            return [exp[0] * exp[1]]