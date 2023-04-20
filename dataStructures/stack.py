# description: implementation of a stack on top of a custom external dynamic array 

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack clas
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        This method adds a new element to the top of the stack.
        
        Param: value: object
        return: None
        """
        # resize the array if its capacity is full
        if self.size() == self._da.get_capacity():
            self._da.resize(self.size()*2)
        
        self._da.append(value)

    def pop(self) -> object:
        """
        This method removes the top element from the stack and returns its value.
        
        Param: None
        return: None
        """
        if self.is_empty():
            raise StackException
        
        value = self._da.get_at_index(self.size()-1)
        # while the remove_at_index() method runs at O(n), because the last index is used as
        # an input here, the for loop in the method is bypassed and the method is run at O(1) complexity.
        self._da.remove_at_index(self.size()-1)

        return value

    def top(self) -> object:
        """
        This method returns the value of the top element of the stack without removing it.
        
        Param:None
        return: None
        """

        if self.is_empty():
            raise StackException
        # return value at the head node
        return self._da.get_at_index(self.size()-1)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
