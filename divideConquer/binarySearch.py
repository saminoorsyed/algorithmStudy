# the following is a recursive binary search
def binary_search(arr, start, end, target):
    if start <= end:
        middle = (start + end) // 2
        print(start,middle, end)
        if arr[middle] == target:
            # found
            return middle

        if arr[middle] > target:
            return binary_search (arr, start, middle-1, target)

        if arr[middle] < target:
            return binary_search(arr, middle+1, end, target)
    # not found
    return -1  


def search(arr, key):
    return binary_search(arr, 0, len(arr)-1, key)

# the following is an iterative binary search from the neetcode selection

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

def binarySearch(nums: list[int], target: int) -> int:
    """
    to perform a binary search on a sorted list, we can use a while loop
    """
    right = len(nums)-1
    left = 0
    while left<=right:
        middle = (right+left)//2
        current = nums[middle]
        if current == target:
            return middle
        if current< target:
            left = middle+1
        else:
            right = middle-1
    return -1


if __name__=="__main__":
    # even length
    numbers = [-1,0,3,5,9,12]
    print(binarySearch(numbers, 5))
    # odd length
    numbers = [1,2,3,4,5,6,7,8,9]
    print(binarySearch(numbers, 5))
    print(binarySearch([0],1))
    print(binarySearch([0],0))
    print(binarySearch([],1))