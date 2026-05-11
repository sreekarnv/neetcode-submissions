class MinStack:

    def __init__(self):
        self.data = []
        self.stack = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.stack:
            self.stack.append(val)
        else:
            self.stack.append(min(val, self.stack[-1]))

    def pop(self) -> None:
        self.data.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.stack[-1]
