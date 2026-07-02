class MinStack:

    def __init__(self):
        self.item = []
        self.minstack =[]
        

    def push(self, value: int) -> None:
        self.item.append(value)
        if not self.minstack or value < self.minstack[-1]:
            self.minstack.append(value)
        else:
            self.minstack.append(self.minstack[-1])
        
    def pop(self) -> None:
        if len(self.item)==0:
            return "Stack Underflow"
        self.item.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.item[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()