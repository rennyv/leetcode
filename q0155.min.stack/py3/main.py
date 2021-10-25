class MinStack:

    def __init__(self):
        self.stack_main = []
        self.stack_min = []

    def push(self, val: int) -> None:
        self.stack_main.append(val)
        if not self.stack_min or self.stack_min[-1] >= val:
            self.stack_min.append(val)

    def pop(self) -> None:
        last = self.stack_main.pop()
        if last == self.stack_min[-1]:
            self.stack_min.pop()

    def top(self) -> int:
        return self.stack_main[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()