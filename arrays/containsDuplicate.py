# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#INTUITION:
# we need to keep a log of all the numbers in the array and check if even one number shows up twice.
# Approach:
# the set function in Python implements a hash that create a "set" of the elements in the list, meaning no duplicates through the use of 
# a hash. if the set is == to the length of the original array, then there is no duplicate
def containsDuplicate(nums:list)-> bool:
    """
    uses python's built in set() function to eliminate duplicates
    this works in O(n) time through the use of hashmap
    """
    return (len(nums)!=len(set(nums)))

if __name__=='__main__':

    number_list = [1,2,5,4,2,9]
    print(containsDuplicate(number_list))
    #should print True
    number_list2 = [0]
    print(containsDuplicate(number_list2))
    # should print false 