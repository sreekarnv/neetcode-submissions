class MinStack:

    def __init__(self):
        self.data = []
        self.stack = []

    def push(self, val: int) -> None:
        self.data.append(val)
        _val = val if len(self.stack) == 0 else min(val, self.stack[-1])
        self.stack.append(_val)

    def pop(self) -> None:
        self.data.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.stack[-1]
