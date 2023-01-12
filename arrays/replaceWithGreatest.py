# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

def replaceElements(arr: list[int]) -> list[int]:
    maximum = arr[-1]
    for index in range(len(arr)-2,-1,-1):
        stored = arr[index]
        arr[index] = maximum
        maximum = max(maximum, stored)
    arr[-1] = -1
    return arr
        

if __name__ =="__main__":
    arr = [17,18,5,4,6,1]
    print(replaceElements(arr))
# Output: [18,6,6,6,1,-1]
    arr = [400]
    print(replaceElements(arr))

# Output: [-1]
# Explanation: There are no elements to the right of index 0.