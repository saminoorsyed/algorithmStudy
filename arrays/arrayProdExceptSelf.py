# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Intuition
# Since we have to do this in O(n) time, we cannot use nested for loops, but we can use multiple for loops in a row

# Approach
# The trick here is to create an answer array that is the same length as nums, then loop through it once from left to right so that each index of answer, contains the product of all of the elements to its left.
# Next, we initialize a variable called product, and loop through the array from right to left, using product to store the cumulative product of the elements that reside to the right of the index in question. Each time product is multiplied to include a new element, the product is multiplied by the associated element in the answer array

# Complexity
# Time complexity:
# the time complexity here is O(n) since we loop through the array only twice

# Space complexity:
# the space complexity is also O(n) since we have to create only one other array and a variable to generate and store the answer

def productExceptSelf(nums: list[int]) -> list[int]:
    """
    
    """
    answer = [1]*len(nums)
    product = 1

    for index in range(1,len(nums)):
        answer[index] = answer[index-1]*nums[index-1]
    
    for index in reversed(range(len(nums)-1)):
        product *= nums[index+1]
        answer[index]*=product
    return answer


if __name__ == '__main__':

    numberList = [1,2,3,4]
    # output should be [24,12,8,6]

    print(productExceptSelf(numberList))