def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    res = [[]]
    for i in range(len(nums)):
        # using res[:] means you get to operate on a copy of res that remains constant
        for numbers in res[:]:
            tmp = [nums[i]] + numbers
            #don't add duplicate permutations
            tmp.sort()
            if (tmp not in res):
                res.append(tmp)
        res.sort()
    return res


if __name__ == "__main__":
    numbers = [1, 2, 2]
    print(subsetsWithDup(numbers))