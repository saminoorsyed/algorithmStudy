# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that
#  they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.


# Intuition:
# this is a two pointer problem because the list is sorted and we are looking for two index values

def twoSum(numbers: list[int], target: int)->list[int]:
    # set the pointers to either end of array
    l = 0
    r = len(numbers) - 1
    while numbers[l]+ numbers[r] != target:
        # if the sum is too large, decrease the right pointer
        if numbers[l]+numbers[r] > target:
            r-= 1
        # If the sum is too small, increment the first pointer
        elif numbers[l]+ numbers[r]< target:
            l+= 1
    return [r+1,l+1]



#Intuition:
# Since this list is sorted, we may be able to use Binary Search to find the difference value that we're looking for rather than creating an entirely new dictionary in O(n) time

# this solution runs in O(nlog(n)) time
def twoSumBinary(numbers: list[int], target: int) -> list[int]:
    # first we begin a loop through each element of the array, keeping track of the index
    for index, el in enumerate(numbers):
    # for each element,  we find the difference that the target has from the element.
        difference = target-el
    # we search for that difference using a binary search on the remaining array
        low = index+1
        high = len(numbers)-1
        middle = (high + low)//2
        while low <= high:
            if numbers[middle] == difference:
                return [index,middle]
            if numbers[middle]> difference:
                high = middle-1
                middle = (low + high)//2
            if numbers[middle]< difference:
                low = middle+1
                middle = (low + high)//2
            

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9

    print(twoSum(nums, target))