class MinStack:

    def __init__(self):
        self.data = []
        self.stack = []

    def push(self, val: int) -> None:
        minval = min(self.stack[-1], val) if self.stack else val

        self.data.append(val)
        self.stack.append(minval)

    def pop(self) -> None:
        self.data.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.stack[-1]
        
