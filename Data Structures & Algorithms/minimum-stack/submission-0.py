'''
I think we can implement a stack by using an array here. The tricky part of this problem
is to implement getMin() while keeping everything in O(1)

we can create a second stack called minStack where we keep track of the min value up to
a certain index
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # reassign min val to next smallest
        if self.minStack:
            val = min(val, self.minStack[-1])
        
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
