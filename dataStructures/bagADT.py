# Description: Implementation of a Bag ADT built over the DynamicArray class defined
# in dynamic_array.py with the following methods: add(), remove(), count(), clear(),
#  equal(), __iter__(), __next__()



from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def get_data(self):
        """
        returns the Dynamic array object
        """
        return self._da

    def add(self, value: object) -> None:
        """
        This method adds a new element to the bag. It must be implemented with O(1)
        amortized runtime complexity.

        Param: value: object
        return: None

        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        This method removes any one element from the bag that matches the provided
        value object. It returns True if some object was actually removed from the bag.
        Otherwise, it returns False.

        Param: value: object
        return: None
        """

        # because the if statement will only run once, this function will have <= O(N) complexity
        # because the number of operations performed is directly proportional to n+1, where n
        # is the size of the array.
        for index in range(self.size()):
            if self._da.get_at_index(index) == value:
                self._da.remove_at_index(index)
                return True
        return False


    def count(self, value: object) -> int:
        """
        This method returns the number of elements in the bag that match the provided value object.

        Param: value: object
        return: int
        """
        count = 0
        for index in range(self.size()):
            if value == self._da.get_at_index(index):
                count +=1
        return count


    def clear(self) -> None:
        """
        This method clears the contents of the bag and resets it's private data_members
        to their default state by calling my previously defined clear() method from
        the DynamicArray.
        
        Param: None
        return: None
        """
        # calls the clear method already defined in the Dynamic array which has O(1) complexity
        self._da.clear()

    def equal(self, second_bag: "Bag") -> bool:
        """
        This method compares the contents of a bag with the contents of a second bag provided as
        a parameter. The method returns True if the bags are equal (contain the same number of
        elements, and also contain the same elements without regard to the order of elements).
        Otherwise, it returns False. calls the count method to check whether the Bags are equivalent.

        Param: second_bag: Bag object
        return: bool
        """
        if self.size() != second_bag.size():
            return False
        if self.size() == 0:
            return True
       
        # Compares the count of each item in bag 1 and bag 2. If the value counts of equally sized arrays don't match 
        # the arrays cannot be the same. One way to optimize could be to create a new array with a list of items
        # that have already been checked and run an if statement to see if an Item has already been checked. This
        # would reduce O(2(n)**2) complexity to O(n**2) complexity for each loop that has a value that has already
        # been checked... unfortunately, extra datastructures were not permitted in the specs. strictly speaking, 
        # O(2(n)**2) complexity and O(n**2) complexity are the same in big O notation, O(n**2)


        for index in range(self.size()):
            if self.count(self._da.get_at_index(index)) != second_bag.count(self._da.get_at_index(index)):
                return False
        return True

    def __iter__(self):
        """
        calls to external iterator class

        """
        return Bag_Iterator(self)

class Bag_Iterator:
    def __init__(self, bag: Bag):
        """
        defines the index and accesses the bag data.
        """
        self._bag = bag
        self._index = 0

    def __iter__(self):
        """
        iterator function.
        """
        return self

    def __next__(self):
        """
        Obtains next value and advances the iterator.
        """
       # I'm very interested in how these dunder methods work. Will have to read some documentation on them
        if self._index >= self._bag.size():
            raise StopIteration
        
        value = self._bag.get_data().get_at_index(self._index)
        self._index += 1
        
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)