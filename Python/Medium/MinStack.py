# Medium Problem
# Problem 155

class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mins and val <= self.mins[-1]:
            self.mins.append(val)
        elif not self.mins:
            self.mins.append(val)

    def pop(self) -> None:
        if self.stack.pop(-1) == self.mins[-1]:
            self.mins.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]