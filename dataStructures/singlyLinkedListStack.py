# Description: Implementation of a stack ADT utilizing a chain of Singly-Linked Nodes
# with the following methods: push(), pop(), top()

from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        """
        out = 'STACK ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        This method adds a new element to the top of the stack. I
        
        Param: value:object
        return: None
        """
        #set new head to a node with the new value and the old head as the next node
        self._head = SLNode(value, self._head)

    def pop(self) -> object:
        """
        This method removes the top element from the stack and returns its value.

        Param: None
        return: None
        """
        if self.is_empty():
            raise StackException
        
        #save value at top of Stack so that it can be returned and then remove it
        value = self._head.value
        self._head = self._head.next
        return value

    def top(self) -> object:
        """
        This method returns the value of the top element of the stack without removing it.
        
        Param: None
        return: None
        """
        if self.is_empty():
            raise StackException
        return self._head.value

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