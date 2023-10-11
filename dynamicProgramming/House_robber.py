# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

def rob(nums: list[int]) -> int:
    """ Here  we take the most we can from each section of the array, looking at houses in pairs of twos"""
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    profit = [0]*(len(nums))
    profit[0] = nums[0]
    profit[1] = nums[1]
    profit[2] = max(nums[2]+ profit[0],profit[1])
    for index in range(3,len(nums)):
        option1 = nums[index]+ profit[index-2]
        option2 = profit[index-1]
        option3 = profit[index - 3] + nums[index]
        profit[index] = max([option1, option2, option3])
    return profit[-1]

print(rob([1,2,3,1]))
