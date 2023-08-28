# sort a list of numbers in ascending order the number of set digits in their binary notation.
def cardinal_sort(nums:list[int])-> list[int]:
    #function to find the cardinality of a number:
    def cardinality(num: int)-> int:
        count = 0
        while num:
            count += num % 2
            num = num//2
        return count
    #sort based on cardinality
    answer = sorted(nums, key = lambda x : cardinality(x))
    return answer
if __name__ == "__main__":
    nums = [1,2,3,4,5]
    # should print [1,2,4,3,5]
    print(cardinal_sort(nums))