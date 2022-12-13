# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.


# using a two pointer solution:
# See two pointer solution for two sum
def threeSum(nums: list[int]) -> list[list[int]]:
    #sort the list in nlogn time
    nums.sort()
    final = {}
    if len(nums)<3 or nums[-1]<0:
        return []
    for index1 in range(len(nums)-2):
        if nums[index1]>0:
            return list(final.keys())
        l = index1+1
        r = len(nums)-1
        total = nums[index1]+nums[l]+nums[r]
        while l<r:
            if total == 0:
                final[(nums[index1], nums[l], nums[r])]= 1
                break
            if total>=0:
                r-=1
            if total<=0:
                l+=1
            total = nums[index1]+nums[l]+nums[r]
    return list(final.keys())

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    print(threeSumDict(nums))

# failed solution using array two sum solution, issue is that does not account for duplicate numbers in original list because of the first hash 
# def threeSumDict(nums:list[int])-> list[list[int]]:
#     final = {}
#     numberLog = {}
#     if len(nums)<3:
#         return []
#     for index, el in enumerate(nums):
#         if el not in numberLog:
#             numberLog[el] = index
#     for in1 in range(len(nums)-2):
#         target = nums[in1]*-1
#         for in2 in range(in1+1,len(nums)-1):
#             difference = target - nums[in2]
#             if difference in numberLog:
#                 addList = sorted([nums[in1], nums[in2], difference])
#                 final[tuple(addList)] =1
#     return list(final.keys())