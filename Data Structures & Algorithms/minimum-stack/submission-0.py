class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.minimum, val)

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
