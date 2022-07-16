def max_independent_set(nums:list)-> list:
    """
    Given a list of numbers, returns a subsequence of non-consecutive numbers in the form of a 
    list that would have the maximum sum. When the numbers are all negatives your code 
    should return [] 
    """
    neg_count = 0
    for element in nums:
        if element < 0:
            neg_count += 1
    if neg_count == len(nums):
        return []
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    cache = [0 for x in range(len(nums))]
    solution = [[] for x in range(len(nums))]
    for index in range(len(nums)):
        if index == 0:
            cache[0] = max(nums[0], 0)
            solution[index]=[max(nums[0], 0)]
        if index == 1:
            cache[1] = max(nums[0], nums[1])
            solution[index]=[max(nums[0], nums[1])]
        else:
            if nums[index] + cache[index-2] > cache[index-1]:
                cache[index] = nums[index] + cache[index-2]
                solution[index] = [nums[index]]+[solution[index-2]]
            else:
                cache[index] = cache[index-1]
                solution[index] = [solution[index-1]]
    print (cache)
    return solution



if __name__ == "__main__":
    test = [7,2,5,8,6] 
    print(max_independent_set(test))