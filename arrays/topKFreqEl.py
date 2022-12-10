# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# create a dictionary b/c we are counting values in an array key:value = number: frequency
# sort the keys of the dictionary using sorted function with key = lambda function to return frequencies
# slice the list

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