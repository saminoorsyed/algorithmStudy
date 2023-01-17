# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

def sortColors(nums: list[int]) -> None:
    red = 0
    white = 0
    blue = 0
    for item in nums:
        if item ==0:
            red+=1
        elif item == 1:
            white +=1
        else:
            blue+=1
    index = 0
    while red>0:
        nums[index] = 0
        red-=1
        index+=1
    while white >0:
        nums[index] = 1
        white-=1
        index+=1
    while blue>0:
        nums[index]=2
        blue-=1
        index+=1

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    sortColors(nums)
    print(nums)
# Output: [0,0,1,1,2,2]
    nums = [2,0,1]
    sortColors(nums)
    print(nums)
# Output: [0,1,2]