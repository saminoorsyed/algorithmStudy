# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# create a dictionary b/c we are counting values in an array key:value = number: frequency
# sort the keys of the dictionary using sorted function with key = lambda function to return frequencies
# slice the list

# Intuition
# Since this is an array grouping problem, using a dictionary like a hash is a good place to start.

# Approach
# once you have your dictionary, the goal is to sort your keys based on their dictionary values. Luckily, the built in "sorted()" function has an option which can be used to specify the sorting criteria. For this criteria I used the lambda function to return the value of each key in my aforementioned dictionary. finally we use list splicing to get our desired results

# Complexity
# Time complexity:
# O(nlog(n)) since Python's sorted() function is likely based on the merge sort

# Space complexity:
# Since we create a dictionary and use the sorted() function the time complexity should be O(n). Meaning we create n*c copies of the data where c is a constant and n is the number of elements of the input array.

def topKFrequent(nums: list[int], k: int) -> list[int]:
    nums_dict = {}
    for el in nums:
        if el not in nums_dict:
            nums_dict[el] = 0
        nums_dict[el]+=1
    orderedList = sorted(list(nums_dict.keys()), key = lambda x: nums_dict[x], reverse=True)
    return orderedList[:k]
if __name__ == '__main__':

    numberList = [2,2,1,1,1,3,3,3,3,3,4]
    kth = 2

    print(topKFrequent(numberList,kth))