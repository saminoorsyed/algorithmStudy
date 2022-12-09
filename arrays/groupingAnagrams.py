# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    create a dictionary and use the sorted anagrams like a hash key to determine how 
    to treat the current anagram: create a new key, or append the item to an old key:value pair
    """
    ana_dict = {}

    for item in strs:
        # create a key that will be the same for each anagram
        key = ''.join(sorted(item))
        # append item to the key:value pair
        if key not in ana_dict:
            ana_dict[key]= []
        ana_dict.get(key).append(item)

    return ana_dict.values()