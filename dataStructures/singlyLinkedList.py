# Name: Sami Noor Syed
# OSU Email: Syeds@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 5/2
# Description: Implementation of a singly linked data structure with the following methods:
# insert_front(), insert_back(), insert_at_index(), remove_at_index(), remove(), count(), find(), slice()


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        This method adds a new node at the beginning of the list (right after the front sentinel).
        Param: value: object
        return: None
        """
        self._head.next = SLNode(value, self._head.next)

    def insert_back(self, value: object) -> None:
        """
        This method adds a new node at the end of the list.
        """
        
        node = self._head
        # iterates through to the last node and adds the 
        while node.next != None:
            node = node.next
        node.next = SLNode(value)
        

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method inserts a new value at the specified index position in the linked list.
        
        Index 0 refers to the beginning of the list (right after the front sentinel). If the provided index is invalid, the method raises a custom “SLLException”. Code for the exception is provided in the skeleton file. If the linked list contains N nodes (the sentinel node is not included in this count), valid indices for this method are [0, N] inclusive.

        """

        if index <0:
            raise SLLException

        node = self._head
        # iterates through the linked list and sets the next value at the specified node to the new node
        for iter in range(index):
            if node.next == None:
                raise SLLException
            node = node.next
        node.next = SLNode(value, node.next)

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the node at the specified index position from the linked list.
        """
        if index < 0 or self.is_empty():
            raise SLLException

        node = self._head
        # loops through the linked list as many times as the index specifies and removes the target node
        for iter in range(index):
            node = node.next
            if node.next == None:
                raise SLLException
        if node.next != None:
            node.next = node.next.next
        else:
            node.next = None

    def remove(self, value: object) -> bool:
        """
        This method traverses the list from the beginning to the end and removes the first node that matches the provided “value” object. The method returns True if a node was removed from the list. Otherwise, it returns False.
        """
        
        node = self._head
        # traverses the singly linked and removes the target node from the chain of nodes
        while node.next != None:
            if node.next.value == value:
                node.next = node.next.next
                return True
            node = node.next
        return False



    def count(self, value: object) -> int:
        """
        This method counts the number of elements in the list that match the provided “value” object. The method then returns this number.
        """
        node = self._head
        count = 0
        # adds one to the count for each value that is = to the input value as it traverses the nodes until it reaches the end.
        while node != None:
            if node.value == value:
                count +=1
            node = node.next
        return count

    def find(self, value: object) -> bool:
        """
        This method returns a Boolean value based on whether or not the provided “value” object exists in the list.
        """
        node = self._head
        # traverses the nodes until one node = the value of the input, then stops.
        while node != None:
            if node.value == value:
                return True
            node = node.next
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        This method returns a new LinkedList object that contains the requested number of nodes from the original list, starting with the node located at the requested start index.

        original list contains N nodes, a valid start_index is in range [0, N - 1] inclusive. The original list cannot be modified. The runtime complexity of your implementation must be O(N). If the provided start index is invalid, or if there are not enough nodes between the start index and the end of the list to make a slice of the requested size, this method raises a custom “SLLException”. Code for the exception is provided in the skeleton file.
        """
        node = self._head.next

         # conditions to identify invalid parameters
        if start_index < 0 or start_index >= self.length() or size < 0 or self.length() - (start_index) < size:
            raise SLLException

        #if we know the last index, we can optimize by running only until we reach the last desired value rather than all the way through the list
        last_index = start_index + size
        count = 0

        NewList = LinkedList()
        for iter in range(last_index):
            if count >= start_index:
                NewList.insert_front(node.value)
            count += 1
            node= node.next

        #reverse the order of the list
        node = NewList._head
        FinalList = LinkedList()
        for iter in range(NewList.length()):
            FinalList.insert_front(node.next.value)
            node=node.next

        return FinalList





if __name__ == '__main__':

    print('\n# insert_front example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_front('A')
    lst.insert_front('B')
    lst.insert_front('C')
    print(lst)

    print('\n# insert_back example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_back('C')
    lst.insert_back('B')
    lst.insert_back('A')
    print(lst)

    print('\n# insert_at_index example 1')
    lst = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_at_index example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)

    print('\n# remove example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# remove example 2')
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# count example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# find example 1')
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Clause"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Clause"))

    print('\n# slice example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print(lst, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(lst, ll_slice, sep="\n")

    print('\n# slice example 2')
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", lst.slice(index, size))
        except:
            print(" --- exception occurred.")