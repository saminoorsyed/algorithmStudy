# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

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