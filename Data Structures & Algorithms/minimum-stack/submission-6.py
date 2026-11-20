class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        self.minimum = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum != None:
            self.minimum = min(self.minimum, val)
        else:
            self.minimum = val
        self.mins.append(self.minimum)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.mins.pop(-1)
        if len(self.stack) > 0:
            self.minimum = self.mins[-1]
        else:
            self.minimum = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
