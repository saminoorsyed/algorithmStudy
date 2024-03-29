# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Approach:
# Here we still use a binary search, but instead of looking for a target number, we are looking for a minimum, so we adjust our middle value to in a manner that moves it toward the smallest value. if the number middle number is greater than the right pointer, we know the smallest number lies to its right, make the left pointer point to 1 greater than the number (since it is higher than another value, it cannot be the min). otherwise, we know that the min lies to the left of the pointer and we can cinch the window to encompass only the numbers smaller <= the middle number. once the left and right pointers are pointing to the same value, we know that value is the lowest (since the left pointer)

def findMin(nums: list[int]) -> int:
    left, right = 0, len(nums)-1
    while left!=right:
        middle = (left +right)//2
        if nums[middle]>nums[right]:
            left = middle+1
        else:
            right = middle
    return nums[left]


if __name__ == "__main__":
    nums = [3,4,5,1,2]
    print(findMin(nums))
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

    nums = [4,5,6,7,0,1,2]
    print(findMin(nums))

# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

    nums = [11,13,15,17]
    print(findMin(nums))

# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
