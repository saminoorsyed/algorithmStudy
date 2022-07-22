def amount(listicle:list, target:int)->list:
    listicle.sort()
    return amount_helper(listicle, target, [],[])

def amount_helper(listicle:list, target: int, permutation: list, solution:list)->list:

    if 0 == target:
        if permutation not in solution:
            solution.append(permutation.copy())
        return
    if listicle == []:
        return []
    for i in range(len(listicle)):
        if listicle[i] <= target:
            remain = target - listicle[i]
            permutation.append(listicle[i])
            amount_helper(listicle[1:], remain, permutation, solution)
            permutation.pop()
    return solution

# below is my first attempt that seemed to work on my local, but did not on gradescope.
# def amount(numbers, target):
#     return amount_helper(numbers, target)
# def amount_helper(numbers: list, target:int, combos: list = [], final: list = [])-> list:
#     """
#     Receives a list of unique items and returns a list of total possible permutations of each item in that list using the backtracking technique
#     """
#     #tabulate the sum of the current combination
    
#     #if the target is met, append the values from the combo to the solution
#     if target == 0:
#         result = [numbers[x] for x in combos]
#         # do not repeat any values
#         result.sort()
#         if result not in final:
#             final.append(result.copy())
#         combos = []
#         return
#     #loop through items in numbers using index values and add the index value if the array element + the sum is <= target
#     for index in range(len(numbers)):
#         # do not repeat elements from the array or add elements to the combo if they cause the sum to > the target
#         # if combos is empty
#         if numbers[index] <= target and not combos:
#             combos.append(index)
#             remain = target- numbers[index]
#             amount_helper(numbers, remain, combos, final)
#             combos.pop()
#         # if combos is not empty only add index values greater than the last index
#         elif combos and index > combos[-1] and numbers[index] <= target:
#             combos.append(index)
#             remain = target- numbers[index]
#             amount_helper(numbers, remain, combos, final)
#             combos.pop()
    
#     return final

# basic tests
if __name__ == '__main__':

    numbers = [11,1,3,2,6,1,5]
    target = 8
    print(amount(numbers,target))
    check_answer = amount(numbers, target)
    count = 0
    for index in range(len(check_answer)):
        shot = sum(check_answer[index])
        # check that each of the answers adds up to the correct target and that it is not repeated in the list afterward
        check_answer[index].sort()
        if shot != target or check_answer[index] in check_answer[index+1:]:
            print (check_answer[index], "it didn't work")
        else:
            count+=1
    print (len(check_answer), count)