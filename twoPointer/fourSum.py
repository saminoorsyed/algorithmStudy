def fourSum(nums: list[int], target: int) -> list[list[int]]:
    result = []
    n = len(nums)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            remaining_target = target - nums[i] - nums[j]
            two_exists = twoSum(nums[j + 1:], remaining_target)
            if two_exists:
                for indices in two_exists:
                    new_res = sorted([nums[i], nums[j]] + indices)
                    if new_res not in result:
                        result.append(new_res)
    return result

def twoSum(nums: list[int], target: int) -> list[list[int]]:
    values = {}
    result = []
    for i, val in enumerate(nums):
        if target - val in values:
            result.append([val, target - val])
        values[val] = i
    return result

# Example usage
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))


if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    target = 0

    print(fourSum(nums, target))