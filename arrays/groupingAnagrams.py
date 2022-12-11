# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# INTUITION:
# since we are grouping or accumulating, we likely want to use a dictionary as we might a hash table.
# Approach:
# In this case we can use the sorted item as a key, and append each new string to the key it generates
# TIME COMPLEXITY:
# since we loop through the list of strings once, we have a time complexity of O(n).
# though there is an extra cost, to sort each item in the list to create a valid hash key, we can treat this
# as a fixed cost that does not affect the overall time complexity. checking if the key is in the dictionary is
# O(1) cost
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