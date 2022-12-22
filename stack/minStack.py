# # Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Approach:
# keep two stacks, and when a lesser or equal min is found, append it to the min stack
# then we can pop values from both stacks when they're equal.

class MinStack:

    def __init__(self) -> None:
        self._minStack = []
        self._stack = []
    
    def push(self, val: int)->None:
        if not self._minStack or val<= self.minStack[-1]:
            self._minStack.append(val)
        self._stack.append(val)
    
    def pop(self)-> None:
        if self._minStack[-1] == self._stack[-1]:
            self._minStack.pop()
        self._stack.pop()
    
    def top(self)->int:
        return self._stack[-1]
    
    def getMin(self)-> int:
        return self._minStack[-1]