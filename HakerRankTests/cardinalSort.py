# sort a list of numbers in ascending order the number of set digits in their binary notation.
def cardinal_sort(nums:list[int])->list[int]:
    """
    returns a list sorted in ascending order by the second value of each inner list
    the inner list comes in the form of [originalValue, cardinality]
    """
    def countOnes(num):
        """
        counts the number of set digits in the binary form of a decimal
        """
        count =0
        while num:
            # when the remainder is one, count should be incremented
            count += num%2
            num = num//2
        return count
    
    arr = [[number, countOnes(number)] for number in nums]
    # use python sorted with a lambda function
    result =  sorted(arr, key = lambda arr:arr[1] )
    return result

# set count ones separate so that I can test it
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