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
# Basic tests for each function
if __name__ == '__main__':
    print(permutation_backtrack(['a', 'b', 'c']))
    print(powerset_backtrack(['a', 'b', 'c']))
    print(perm_sum_backtrack([2,3,6,7], 7))