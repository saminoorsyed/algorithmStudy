def permutation_backtrack(set: list, permutations: list = [], result: list = [])-> list:
    """
    Receives a list of unique items and returns a list of total possible permutations of each item in that list using the backtracking technique
    """
    if len(permutations) == len(set):
        result.append(permutations.copy())
        permutations = []
        return

    for item in set:
        if item not in permutations:
            permutations.append(item)
            permutation_backtrack(set, permutations, result)
            permutations.pop()

    return result
def powerset_backtrack(set: list, permutations: list = [], result: list = [])-> list:
    """
    Receives a list of unique items and returns a list of total possible permutations of each item in that list using the backtracking technique
    """
    if permutations not in result:
        result.append(permutations.copy())
        if  len(permutations) == len(set):
            permutations = []
            return

    for item in set:
        if item not in permutations:
            permutations.append(item)
            powerset_backtrack(set, permutations, result)
            permutations.pop()

    return result

def perm_sum_backtrack(set: list, target:int, permutations: list = [], result: list = [])-> list:
    """
    Receives a list of unique items and returns a list of total possible permutations of each item in that list using the backtracking technique
    """
    sum = 0
    for item in permutations:
        sum+= item
    
    if sum == target:
        result.append(permutations.copy())
        permutations = []
        return

    for item in set:
        if sum + item <= target:
            permutations.append(item)
            
            perm_sum_backtrack(set, target, permutations, result)
            permutations.pop()
    
    return result

def combo_sum_backtrack(set: list, target:int, combos: list = [], final: list = [])-> list:
    """
    Receives a list of unique items and returns a list of total possible permutations of each item in that list using the backtracking technique
    """
    #tabulate the sum of the current combination
    sum = 0
    for index in range(len(combos)):
        sum+= set[combos[index]]
    
    #if the target is met, append the values from the combo to the solution
    if sum == target:
        result = [set[x] for x in combos]
        final.append(result.copy())
        combos = []
        return
    #loop through items in set using index values and add the index value if the array element + the sum is <= target
    for index in range(len(set)):
        # do not repeat elements from the array or add elements to the combo if they cause the sum to > the target
        # if combos is empty
        if sum + set[index] <= target and not combos:
            combos.append(index)
            combo_sum_backtrack(set, target, combos, final)
            combos.pop()
        # if combos is not empty only add index values greater than the last index
        elif combos and index > combos[-1] and sum +set[index] <= target:
            combos.append(index)
            combo_sum_backtrack(set, target, combos, final)
            combos.pop()
    
    return final

# Basic tests for each function
if __name__ == '__main__':
    # print(permutation_backtrack(['a', 'b', 'c']))
    # print(powerset_backtrack(['a', 'b', 'c']))
    # print(perm_sum_backtrack([2,3,5,7], 7))
    print(combo_sum_backtrack([11, 1, 3, 2, 6, 1, 5], 8))