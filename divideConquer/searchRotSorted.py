# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Intuition
# go through each situation, and map out the conditionals, use a list of 5 or 6 items to give yourself room to see all the potential situations.

# Approach
# Here we can map out each situation in which the left and right pointers should move to middle +1 and middle-1. the first is if the left pointer is at a number lower than the middle number. if the target lies between those two (ie [1,2,3,4,5,6] target = 3), move the right pointer to the middle - 1. otherwise, nmove the left pointer to the middle +1. we do the same for the situation in which the left pointer> than the middle pointer. here if the target is less than the middle, or greater than the left, (ie [6,7,1,2,3,4,5] target = 7 or 1) we move the right pointer to middle - 1 otherwise the left pointer should move up. here, I used the elif statement so that the code would shortcut to else if it were not true... for some reason it speed up my code tremendously from using else: if: else: in the second outer conditional.

def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)-1
    while left <= right:
        middle = (left+right)//2
        if target == nums[middle]:
            return middle
        if nums[left]<= nums[middle]:
            if target>=nums[left] and target<nums[middle]:
                right = middle-1
            else:
                left = middle +1
        else:
            if (target< nums[middle] or target>= nums[left]):
                right = middle - 1
            else: #nums[left]> nums[middle] and target> nums[middle] and target <= nums[left]:
                left = middle +1
    return -1



if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(search(nums, target))
# Output: 4
    nums = [4,5,6,7,0,1,2]
    target = 3
    print(search(nums, target))
# Output: -1
    nums = [1,3]
    target = 3
    print(search(nums, target))
# Output: -1