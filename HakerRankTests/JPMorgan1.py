def cardinal_sort(nums:list[int])->list[int]:
    def countOnes(num):
        count =0
        while num:
            count += num%2
            num = num//2
        return count
    
    arr = [[number, countOnes(number)] for number in nums]

    result =  sorted(arr, key = lambda arr:arr[1] )
    return result
def countOnes(num):
        count =0
        while num:
            count += num%2
            num = num//2
        return count
if __name__ == "__main__":
    nums = [1,2,3,4,5]
    print(cardinal_sort(nums))

    print (countOnes(5))