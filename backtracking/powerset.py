def powerSetBacktrack(set: list, permutations: list = [], result: list = [])-> list:
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
            powerSetBacktrack(set, permutations, result)
            permutations.pop()

    return result

if __name__ == '__main__':
    print(powerSetBacktrack(['a', 'b', 'c']))