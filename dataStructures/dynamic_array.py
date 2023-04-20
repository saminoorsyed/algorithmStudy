# Description: implementation of a Dynamic Array class based on an external static array with the following methods: 
# resize(), append(), insert_at_index(), remove_at_index(), slice(), merge() map(), filter(), reduce()

from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------
    def check_size(self) ->None:
        """
        Method that checks and adjusts the size of the dynamic array to reflect the
        how many indicies have a value other than None

        Param: None
        return: None
        """

        #check and adjust the size of the the array
        for item in range(self._size, self._data.length()-1):
            if self._data.get(item) != None:
                self._size +=1


    def resize(self, new_capacity: int) -> None:
        """
        This method changes the capacity of the underlying storage for the array elements
        by creating a new array with the specified capacity and copying elements from the 
        current array into it.

        param: new_capacity :int
        return: None

        """
        # use check_size() to adjust size of array before append() is implemented
        # self.check_size()

        # Cases in which the method will not work and immediately exit
        if new_capacity < self._size or new_capacity < 1:
            return
        # Create a new Dynamic Array with the specified capacity
        NewArray = StaticArray(new_capacity)
        
        # Copy elements into new array
        for index in range(self._size):
            NewArray.set(index, self._data.get(index))
        
        self._data = NewArray
        self._capacity = new_capacity

        

    def append(self, value: object) -> None:
        """
        Method that adds a value to the end of a a dynamic array object. If the object is full, 
        the capacity of the Dynamic Array should be doubled by calling the resize method

        Param: value: object
        return: None
        """
        if self._size == self._capacity:
            self.resize(self._capacity*2)
        
        self._data.set(self._size, value)
        self._size += 1


    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method adds a new value at the specified index in the dynamic array. Index 0 refers
        tothe beginning of the array. If the provided index is invalid, the method raises a custom
        “DynamicArrayException”.

        Param: index: int, value: object
        return: None
        """
        # adjusts the size for the new Array
        if self._size == self._capacity:
            self.resize(self._capacity*2)

        if index < 0 or index > self._size:
            raise DynamicArrayException
        # loop through each value from the specified insert index and reset it according to it's new index
        self._size += 1
        for item in range(index, self._size):
                saved_value = self._data.get(item)
                self._data.set(item, value)
                value = saved_value
            

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the element at the specified index in the 
        dynamic array. Index 0 refers to the beginning of the array.

        Param: index = int
        return: None
        """

        # cases for invalid index value
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        
        #change capacity of array if needed
        if self._size < self._capacity/4 and self._capacity > 10:
            if self._size * 2 <= 10:
                self.resize(10)
            if self._size* 2 > 10:
                self.resize(self._size *2)

        self._size -= 1
        # adjust each item forward after the removed value in the array once
        for item in range(index, self._size):
            next_value = self._data.get(item+1)
            self._data.set(item, next_value)
        self._data.set(self._size, None)
        


    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        This method returns a new Dynamic Array object that contains the
        requested number of elements from the original array, starting with 
        the element located at the requested start index. 

        Param: start_index :int, size : int
        Return: DynamicArray object

        """
        # conditions to identify invalid parameters
        if start_index < 0 or start_index >= self._size or size < 0 or self._size - (start_index) < size:
            raise DynamicArrayException
        
        # iterating through the start index and ending at the end of the slice,
        # append each item from the old array to a new array
        NewDynamicArray = DynamicArray()
        for index in range(start_index, start_index+size):
            NewDynamicArray.append(self.get_at_index(index))
        
        return NewDynamicArray

    def merge(self, second_da: "DynamicArray") -> None:
        """
        This method takes another Dynamic Array object as a parameter, and
        appends all elements from this other array onto the current one, in
        the same order as they are stored in the array parameter.

        Param: DynamicArray object
        Return: None
        """
        # loop through second array and append it to the first array
        for index in range(second_da.length()):
            self.append(second_da.get_at_index(index))


    def map(self, map_func) -> "DynamicArray":
        """
        This method creates a new Dynamic Array where the value of each element
        is derived by applying a given map_func to the corresponding value from
        the original array.

        Param: map_func: lambda function
        return: Dynamic array object

        """
        # Apply function to each item in the Array and append that value to a new DynamicArray object
        NewDynamicArray = DynamicArray()
        for index in range(self._size):
            new_val = (map_func)(self.get_at_index(index))
            NewDynamicArray.append(new_val)

        return NewDynamicArray


    def filter(self, filter_func) -> "DynamicArray":
        """
        This method creates a new Dynamic Array populated only with those elements
        from the original array for which filter_func returns True.

        Param: filter_func: function
        return: DynamicArray object
        """

        # Apply filter function to each value in the Dynamic array and only append those which return true to a New Dynamic array
        NewDynamicArray = DynamicArray()
        for index in range(self._size):
            if filter_func(self.get_at_index(index)):
                NewDynamicArray.append(self.get_at_index(index))

        return NewDynamicArray
        

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This method sequentially applies the reduce_func to all elements of the
        Dynamic Array, and returns the resulting value. It takes an optional
        initializer parameter. If this parameter is not provided, the first value
        in the array is used as the initializer. If the Dynamic Array is empty, 
        the method returns the value of the initializer (or None, if one was not provided).

        Param: reduce_func: lambda func, initializer, intializer: None or int
        Return: int
        """
        # if the DynamicArray object is empty, return the initializer 
        if self.length() == 0:
            return initializer
        # cases to determine the initializer value
        if initializer == None:
            reduction = self.get_at_index(0)
        # when the initializer value is present, reduction function must be applied to the value at index 0
        if initializer != None:
            reduction = (reduce_func)((initializer),(self.get_at_index(0)))
        for index in range(1, self._size):
            reduction = (reduce_func)((reduction),(self.get_at_index(index)))
        return reduction

    def clear(self) -> None:
        """
        this method clears all the elements in a the Dynamic array
        Param: None
        return: None

        """
        # reset the DynamicArray private data members to represent an empty array with the appropriate capacity
        self._data = StaticArray(4)
        self._size = 0
        self._capacity = 4
        self.resize(4)


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    function that receives a DynamicArray that is sorted in order.
    The function will return a tuple containing (in this order) a
    DynamicArray comprising the mode (most-occurring) value/s in
    the array, and an integer that represents the highest frequency
    (how many times they appear).

    Param: arr: DynamicArray object
    return: tuple : (DynamicArray object, int)
    """
    NewDynamicArray = DynamicArray()
    mode_freq = 1
    current_freq = 1

    for index in range(1, arr.length()):
        # counts the number of times an element shows up in a sorted list
        if arr.get_at_index(index) == arr.get_at_index(index-1):
            current_freq += 1
        # resets the count once the current elemement is different than the last element
        if arr.get_at_index(index) != arr.get_at_index(index-1):
            current_freq = 1
        # appends the new item to the list if it has the same freq as the current mode 
        if mode_freq == current_freq:
            NewDynamicArray.append(arr.get_at_index(index))
        # If a new item has a higher frequency than the current mode, then the array of
        # old modes are cleared from NewDynamicArray object and the new value is appended
        if current_freq > mode_freq:
            NewDynamicArray.clear()
            NewDynamicArray.append(arr.get_at_index(index))
            mode_freq = current_freq
    # if every item showed up only once, add in the first Item, which has not been included yet
    if mode_freq == 1:
        NewDynamicArray.insert_at_index(0,arr.get_at_index(0))

    return (NewDynamicArray, mode_freq) 



# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
