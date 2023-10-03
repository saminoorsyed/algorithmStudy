""" permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
Given an array of integers nums, find the next permutation of nums.
"""
def nextPermutation(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for index in range(len(nums)-1,0,-1):
        if nums[index] > nums[index-1]:
            j = index + 1
            # find the last number that is greater than the previous index
            while j <len(nums) and nums[j]> nums[index-1]:
                j+=1
            nums[index-1], nums[j-1] = nums[j-1], nums[index-1]
            nums[index:] = nums[len(nums)-1: index-1:-1]
    return nums.reverse()

print(nextPermutation([2,1,3]))