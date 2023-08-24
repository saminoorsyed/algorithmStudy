def combinationSum( candidates: list[int], target: int) -> list[list[int]]:
    result = []
    def backtrack(start, combo, new_sum):
        if new_sum == target:
            combo.sort()
            if combo not in result:
                result.append(combo.copy())
            return
        min_value = min(candidates[start:])
        if min_value + new_sum > target:
            return
        for index in range(start, len(candidates)):
            combo.append(candidates[index])
            new_sum += candidates[index]
            backtrack(index, combo, new_sum)
            new_sum -= candidates[index]
            combo.remove(candidates[index])
    backtrack(0,[],0)
    return result




# terrible run time here
# def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
#     result = []
#     def backtrack(combo, new_sum):
#         if new_sum == target:
#             combo.sort()
#             if combo not in result:
#                 result.append(combo.copy())
#             return
#         if new_sum > target:
#             return
#         for el in candidates:
#             combo.append(el)
#             new_sum += el
#             backtrack(combo, new_sum)
#             new_sum -= el
#             combo.remove(el)
#     backtrack([],0)
#     return result

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    print(combinationSum(candidates, target))
