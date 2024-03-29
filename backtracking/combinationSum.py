def combo_sum_backtrack(nums: list, target:int, combos: list = [], final: list = [])-> list:
    """
    Receives a list of unique items and returns a list of total possible permutations of each item in that list using the backtracking technique
    """
    #tabulate the sum of the current combination
    sum = 0
    for index in range(len(combos)):
        sum+= nums[combos[index]]
    
    #if the target is met, append the values from the combo to the solution
    if sum == target:
        result = [nums[x] for x in combos]
        final.append(result.copy())
        combos = []
        return
    #loop through items in nums using index values and add the index value if the array element + the sum is <= target
    for index in range(len(nums)):
        # do not repeat elements from the array or add elements to the combo if they cause the sum to > the target
        # if combos is empty
        if sum + nums[index] <= target and not combos:
            combos.append(index)
            combo_sum_backtrack(nums, target, combos, final)
            combos.pop()
        # if combos is not empty only add index values greater than the last index
        elif combos and index > combos[-1] and sum +nums[index] <= target:
            combos.append(index)
            combo_sum_backtrack(nums, target, combos, final)
            combos.pop()
    return final

# Basic tests for each function
if __name__ == '__main__':
    print(combo_sum_backtrack([2,5,2,1,2], 5))
    print(combo_sum_backtrack([11, 1, 3, 2, 6, 1, 5], 8))
    
