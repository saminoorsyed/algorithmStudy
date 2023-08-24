def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    results = []
    def backtrack(pool, combination, new_target):
        if new_target == 0:
            solution = sorted(combination)
            if solution not in results:
                results.append(solution)
                return
        if new_target < 0:
            return
        for  i, el in enumerate(pool):
            combination.append(el)
            backtrack(pool[i+1:], combination, new_target-el)
            combination.pop()
    backtrack(candidates[:], [],target)
    return results


if __name__ == "__main__":
    candidates = [2,5,2,1,2]
    target = 5
    print(combinationSum2(candidates, target))