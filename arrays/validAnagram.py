# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# INTUITION:
# there are likeley multiple ways to solve this problem, but the basic idea is that we need to sort each string and see if it is
# equal to the other sorted string. the sorted() function in python is an nlog(n) time complexity
def isAnagram(s:str, t:str)-> bool:
    " utilizes built in sorted to compare s and t"
    return sorted(s)==sorted(t)

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    print(isAnagram(s, t))
    # should print True
    s = 'car'
    t = 'rat'
    print(isAnagram(s, t))
    # should print False