def permute(nums: list[int]) -> list[list[int]]:

    ans = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        ans.extend(perms)
        nums.append(n)

    return ans

if __name__ == "__main__":
    numbers = [1,2,3]
    print(permute(numbers))