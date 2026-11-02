class MinStack:

    def __init__(self):
        self.minStack = []
        self.smallest = []
      

    def push(self, value: int) -> None:
        self.minStack.append(value)
        if not self.smallest:
            note = value
        else:
            note = min(value, self.smallest[-1])
        self.smallest.append(note)
       

    def pop(self) -> None:
        self.minStack.pop()
        self.smallest.pop()

       

    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        return self.smallest[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()