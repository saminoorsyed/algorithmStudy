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

if __name__ == '__main__':
    print(perm_sum_backtrack([2,3,5,7], 7))