# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


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