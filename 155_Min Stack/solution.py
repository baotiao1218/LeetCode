class MinStack:

    def __init__(self):
        self.stk = []
        self.min = [sys.maxsize]

    def push(self, val: int) -> None:
        self.stk.append(val)
        if val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        if self.stk[-1] == self.min[-1]:
            self.min.pop()
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()