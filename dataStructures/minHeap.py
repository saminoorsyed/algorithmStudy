# Due Date:5/23
# Description: Implementation of a Min Heap with the following methods: add(), is_empty(), get_min(), remove_min(), build_heap(), size(), clear(), heapsort()

from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        This method adds a new object to the MinHeap while maintaining heap property.

        Param: node: object
        return: None

        """
        if self.is_empty():
            self._heap.append(node)
            return
        # Put the new element at the end of the array.
        self._heap.append(node)
        # Compute the inserted element’s parent index, (i − 1) / 2.
        added_index = self._heap.length() - 1
        parent_index = self.parent(added_index)
        # Compare the value of the inserted element with the value of its parent.
        # If the value of the parent is greater than the value of the inserted element, swap
        # Do not repeat if the element has reached the beginning of the array or if the element is larger than its parent.
        while parent_index >= 0 and self._heap.get_at_index(parent_index) > node:
            self._heap.swap(parent_index, added_index)
            added_index = parent_index
            parent_index = (added_index - 1)//2


    def is_empty(self) -> bool:
        """
        This method returns True if the heap is empty; otherwise, it returns False. The runtime complexity of this implementation must be O(1).

        Param: None
        return: bool
        """
        #use the Dynamic array method to check if the heap is empty
        if self._heap.is_empty():
            return True
        return False

    def get_min(self) -> object:
        """
        This method returns an object with the minimum key, without removing it from the heap. If the heap is empty, the method raises a MinHeapException. The runtime complexity of this implementation must be O(1)

        """
        if self.is_empty():
            raise MinHeapException()
        return self._heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        This method returns an object with the minimum key, and removes it from the heap. If the heap is empty, the method raises a MinHeapException. For the downward percolation of the replacement node: if both children of the node have the same value (and are both smaller than the node), swap with the left child. The runtime complexity of this implementation must be O(log N).

        Param: None
        return: object
        """
        if self.is_empty():
            raise MinHeapException()
        # store the minimum value to return at the end
        min_value = self._heap.get_at_index(0)
        last_array_index = self._heap.length()-1
        # replace the minimum value with the last value
        self._heap.swap(0, last_array_index)
        # remove the new last value of the heap which was the previous minimum value runs at O(1) becuase it does not have to iterate through the whole array
        self._heap.remove_at_index(last_array_index)
        # percolate the new root value of the heap down this has a runtime complexity of O(log N)
        self._percolate_down(0)

        return min_value

    def build_heap(self, da: DynamicArray) -> None:
        """
        This method receives a Dynamic Array with objects in any order, and builds a proper MinHeap from them. The current content of the MinHeap is overwritten.

        Param: da: Dynamic Array
        return: None
        """
        self.clear()

        # this outer loop runs in O(N) time 
        for index in range(da.length()):
            new_item = da.get_at_index(index)
            self._heap.append(new_item)
        # this loop also runs in O(N) time because we start the process at the parent node which is (n-1)//2. any perlocation that occurs will take fewer operations than (n-1)//2 resulting in a total runtime of O(n)
        parent = self.parent(da.length()-1)
        for index in range(parent,-1,-1):
            self._percolate_down(index)
        
    def size(self) -> int:
        """
        This method returns the number of items currently stored in the heap. The runtime complexity of this implementation is O(1).

        Param: None
        return: int
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        This method clears the contents of the heap. The runtime complexity of this implementation is O(1).

        Param: None
        return: None

        """
        self._heap = DynamicArray()

    def _percolate_down(self, parent: int) -> None:
        """
        this method perlocates the top element of the minheap all the way down to the bottom element with O(log N)

        Param: da: DynamicArray, parent: int
        return: None
        """
        # if the heap is empty, stop
        if self.is_empty():
            return
        
        # assign the parent value from its index
        parent_value = self._heap.get_at_index(parent)
        # assign lowest child so that the perlocation loop begins
        lowest_child_index = self.lowest_child(parent)
        lowest_child_value = self._heap.get_at_index(lowest_child_index)
        while parent_value > lowest_child_value:
            self._heap.swap(parent, lowest_child_index)
            # find the index of the new lowest child
            parent = lowest_child_index
            lowest_child_index = self.lowest_child(parent)
            lowest_child_value = self._heap.get_at_index(lowest_child_index)

    def left_child(self, index: int)-> int:
        """ 
        returns the index of the left child of the input node

        Param: index: int
        return: int
        """
        return 2*index + 1
    
    def right_child(self, index: int)-> int:
        """ 
        returns the index of the right child of the input node

        Param: index: int
        return: int
        """
        return 2*(index + 1)

    def parent(self, index: int) -> int:
        """
        Given the index of a child's node, this function returns that node's parent

        Param: index: int
        return: int
        """
        if index == 0:
            return 0

        return (index-1)//2
    
    def lowest_child(self, parent: int) -> int:
        """
        given a parent node's index, this functions returns the index of it's lowest child. if there are no child nodes, then return the parent node's index. If the two child nodes have the same value, then the left child is the new child.

        param: parent: int
        return: int
        """
        # find the index of both children
        right_child = self.right_child(parent)
        left_child = self.left_child(parent)
        last_array_index = self._heap.length() - 1
        # assign the values for each of the children
        # assign the lowest child's value of the parent node if the left node is les than or equal to the right node, then the left node is the lowest child
        if right_child <= last_array_index and left_child <= last_array_index:
            right_child_value = self._heap.get_at_index(right_child)
            left_child_value = self._heap.get_at_index(left_child)
            if left_child_value > right_child_value:
                lowest_child_index = right_child
            else:
                lowest_child_index = left_child
        # if there is no right node, then the lowest child value should be the left node
        elif left_child <= last_array_index:
            lowest_child_index = left_child
        # if there are no child nodes then return the parent's value in order to stop any perlocation loops
        else:
            lowest_child_index = parent
        
        return lowest_child_index


def _percolate_down(last_heap_index: int ,da: DynamicArray(), parent: int) -> None:
        """
        this method is a helper function of heapsort() and perlocates the top element of the minheap all the way down to the bottom of the remaining heap.

        Param: last_heap_index: int, da: DynamicArray, parent: int
        return: None
        """
        # if the array is empty, stop
        if last_heap_index == 0:
            return
        
        # assign the parent value from its index
        parent_value = da.get_at_index(parent)
        # assign lowest child 
        lowest_child_index = _lowest_child(last_heap_index, da, parent)
        lowest_child_value = da.get_at_index(lowest_child_index)
        while parent_value > lowest_child_value and lowest_child_index <= last_heap_index:
            da.swap(parent, lowest_child_index)
            # reassign the parent index to the newest child index and find the new lowest child of the new parent node
            parent = lowest_child_index
            lowest_child_index = _lowest_child(last_heap_index, da, parent)
            lowest_child_value = da.get_at_index(lowest_child_index)

def _left_child(index: int)-> int:
    """ 
    returns the index of the left child of the input node

    Param: index: int
    return: int
    """
    return 2*index + 1

def _right_child(index: int)-> int:
    """ 
    returns the index of the right child of the input node

    Param: index: int
    return: int
    """
    return 2*(index + 1)

def _parent(index: int) -> int:
    """
    Given the index of a child's node, this function returns that node's parent

    Param: index: int
    return: int
    """
    if index == 0:
        return 0

    return (index-1)//2

def _lowest_child(last_heap_index: int, da: DynamicArray(), parent: int) -> int:
    """
    Given a parent node's index, this functions returns the index of it's lowest child. If there are no child nodes, then return the parent node's index.

    param: parent: int
    return: int
    """
    # find the index of both children
    right_child = _right_child(parent)
    left_child = _left_child(parent)
    # assign the values for each of the children
    # assign the lowest child's value of the parent node
    if right_child <= last_heap_index and left_child <= last_heap_index:
        right_child_value = da.get_at_index(right_child)
        left_child_value = da.get_at_index(left_child)
        if left_child_value > right_child_value:
            lowest_child_index = right_child
        else:
            lowest_child_index = left_child
    # if there is no right node, then the lowest child value should be the left node
    elif left_child <= last_heap_index:
        lowest_child_index = left_child
    # if there are no child nodes then return the parent's value in order to stop any perlocation loops
    else:
        lowest_child_index = parent
    
    return lowest_child_index


def heapsort(da: DynamicArray) -> None:
    """
    Write a function that receives a DynamicArray and sorts its content in non-ascending order, using the Heapsort algorithm. You must sort the array in place, without creating a new array. This method does not return anything. You may assume that the input array will contain at least one element, and that values stored in the array are all of the same type (either all numbers, or strings, or custom objects, but never a mix of these).You do not need to write checks for these conditions.

    Param: da: DynamicArray
    return: None
    
    """
    last_array_index = da.length() - 1
    last_heap_index = last_array_index

    # build a heap from the unsorted array in O(n) time
    parent = _parent(last_array_index)
    last_heap_index = last_array_index
    for index in range(parent,-1,-1):
        _percolate_down(last_array_index, da,index)
    # swap the first and last element of the heap, reduce the size of the heap by one index and perlocate the top element down to the end of the heap. repeat the process until the heap is empty
    while last_heap_index > 0:
        da.swap(0, last_heap_index)
        last_heap_index -= 1
        _percolate_down(last_heap_index, da, 0)

        




# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)
    h.add(1000)
    print (h)
    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
