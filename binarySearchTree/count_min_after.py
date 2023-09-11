
def countSmaller(nums: list[int]) -> list[int]:
    counts = [0]*len(nums)
    nums_sorted = []
    for j in reversed(range(len(nums))):
        i = find_index(nums_sorted, nums[j])
        nums_sorted.insert(i,nums[j])
        counts[j] = i
    return counts
def find_index(sorted_arr, num):
    left = 0
    right = len(sorted_arr)-1
    while left <= right:
        middle = left + (right-left)//2
        if sorted_arr[middle]== num:
            return middle
        elif sorted_arr[middle] < num:
            left = middle + 1
        else:
            right = middle - 1
    return left

if __name__ == "__main__":
    nums = [5,2,6,1]
    print(countSmaller(nums))