def amount(numbers: list, target:int, combos: list = [], final: list = [], combo_list: list = [])-> list:
    """
    Receives a list of unique items and returns a list of total possible permutations of each item in that list using the backtracking technique
    """
    #tabulate the sum of the current combination
    sum = 0
    for index in range(len(combos)):
        sum+= numbers[combos[index]]
    
    #if the target is met, append the values from the combo to the solution
    if sum == target:
        result = [numbers[x] for x in combos]
        result.sort()
        if result not in final:
            final.append(result.copy())
        combos = []
        return
    #loop through items in numbers using index values and add the index value if the array element + the sum is <= target
    for index in range(len(numbers)):
        # do not repeat elements from the array or add elements to the combo if they cause the sum to > the target
        # if combos is empty
        if sum + numbers[index] <= target and not combos:
            combos.append(index)
            amount(numbers, target, combos, final)
            combos.pop()
        # if combos is not empty only add index values greater than the last index
        elif combos and index > combos[-1] and sum +numbers[index] <= target:
            combos.append(index)
            amount(numbers, target, combos, final)
            combos.pop()
    
    final = [list(x) for x in final]
    return final

if __name__ == '__main__':
    a = [1,1,2,3,5]
    target = 6
    print(amount(a, target))