class Solution:
    def isValid(self, s: str) -> bool:
        # if open: add to stack
        # if close: remove from stack 
        close_to_open = {"}": "{", "]": "[", ")": "(",}
        # open_to_close = {"{": "}", "[": "]", "(": ")",}
        stack = []
        opens = set("{", "(", "{")

        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if stack.pop(-1) == close_to_open(c):
                    continue
                return False
        return True
