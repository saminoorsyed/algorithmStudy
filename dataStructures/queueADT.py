
# 5/2/22
# Description: Implementation of a Queue ADT class that uses a circular buffer with the following methods:
# engueue(), dequeue(), and front()


from static_array import StaticArray


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    """
    pass


class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue based on Static Array
        """
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        """
        size = self._current_size
        out = "QUEUE: " + str(size) + " element(s). ["

        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa[front_index]) + ', '
            front_index = self._increment(front_index)

        if size > 0:
            out += str(self._sa[front_index])

        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        """
        return self._current_size == 0

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        """
        return self._current_size

    def _increment(self, index: int) -> int:
        """
        Move index to next position
        """

        # employ wraparound if needed
        index += 1
        if index == self._sa.length():
            index = 0

        return index

    # -----------------------------------------------------------------------
    
    def enqueue(self, value: object) -> None:
        """
        This method adds a new value to the end of the queue.
        """
        # doubles the queue if the underlying data structure is full
        if self.size() == self._sa.length():
            self._double_queue()
        # increases the size, incriments the back indicator to the new back index. Also, appends the new value to the back of the Array
        self._current_size += 1
        self._back = self._increment(self._back)
        self._sa.set(self._back, value)


    def dequeue(self) -> object:
        """
        This method removes and returns the value at the beginning of the queue.
        """
        if self.is_empty():
            raise QueueException
        # saves value at eginning of queue, clears that value, then incriments the front of queue indicator, finally reduces current size indicator
        value = self._sa.get(self._front)
        self._sa.set(self._front, None)
        self._front = self._increment(self._front)
        self._current_size -= 1

        return value
        


    def front(self) -> object:
        """
        This method returns the value of the front element of the queue without removing it.
        """
        if self.is_empty():
            raise QueueException

        return self._sa.get(self._front)

    def _double_queue(self) -> None:
        """
        This method changes the capacity of the underlying storage for the array elements
        by creating a new array with the specified capacity and copying elements from the 
        current array into it.

        param: new_capacity :int
        return: None

        """
        # Create a new Dynamic Array with the specified capacity
        NewArray = StaticArray(self.size()*2)
        
        # Copy elements into new array
        for index in range(self.size()):
            # using the percent operator to wrap around the old array so that it can be re-assigned according to the correct indeces (helpful tip from Assignment 1 grading. Thank you!)
            NewArray.set(index, self._sa.get((index + self._front) % (self.size())))
        # set the front indicator back to 0 and the back to the length of the new node
        self._front = 0
        self._back = self.size()-1
        self._sa = NewArray


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
    for i in range(q.size() + 1):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
    for value in [6, 7, 8, 111, 222, 3333, 4444]:
        q.enqueue(value)
    print(q)

    print('\n# front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
