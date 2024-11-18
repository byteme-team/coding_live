class MinStack:
    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if(self.stack[-1] == self.min_stack[-1]):
            self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    
minstack = MinStack()
minstack.push(-2)
minstack.push(0)
minstack.push(-3)
print(minstack.getMin())
minstack.pop()
print(minstack.top())
print(minstack.getMin())