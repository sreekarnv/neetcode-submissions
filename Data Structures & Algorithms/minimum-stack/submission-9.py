class MinStack:

    def __init__(self):
        self.data = []
        self.stack = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.stack) > 0:
            self.stack.append(min(self.stack[-1], val))
        else:
            self.stack.append(val)

    def pop(self) -> None:
        self.data.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.stack[-1]
