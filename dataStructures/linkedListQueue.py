# Due Date: 5/2/2022
# Description: Implementation of a Queue ADT class utilizing a chain of Singly-Linked Nodes with the following methods:
# enque(), dequeue(), front()


from SLNode import SLNode


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        """
        out = 'QUEUE ['
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
        Return True is the queue is empty, False otherwise
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        This method adds a new value to the end of the queue. It must be implemented with O(1) runtime complexity.
        
        Param: value: object
        return: None
        """
        if self.is_empty():
            self._tail = SLNode(value)
            self._head = self._tail
            return
        # create a new node and set it as the new tail after setting the previous tail's next value to the new node
        node = SLNode(value)
        self._tail.next = node
        self._tail = node

    def dequeue(self) -> object:
        """
        This method removes and returns the value from the beginning of the queue

        Param: None
        return: object
        """
        if self.is_empty():
            raise QueueException
        # store the specified value and remove it from the queue 
        value = self._head.value
        self._head = self._head.next

        return value

        

    def front(self) -> object:
        """
        This method returns the value of the front element of the queue without removing it.

        Param: None
        return: int
        """
        if self.is_empty():
            raise QueueException
        
        value = self._head.value

        return value

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)