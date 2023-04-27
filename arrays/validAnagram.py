# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# INTUITION:
# there are likely multiple ways to solve this problem, but the basic idea is that we need to sort each string and see if it is
# equal to the other sorted string. the sorted() function in python is an nlog(n) time complexity
def isAnagram(s:str, t:str)-> bool:
    " utilizes built in sorted to compare s and t"
    return sorted(s)==sorted(t)

# this solution also works, but in run time it takes much longer to complete. strangley, its big O time = O(n) rather than O(nlog(n)) like the above solution
def isAnagramLong(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    anaDict = {}
    for char in s:
        anaDict[char] = anaDict.get(char, 0)+1
    for char in t:
        anaDict[char] = anaDict.get(char, 0) - 1
        if anaDict[char]<0:
            return False
        
    return True

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    print(isAnagram(s, t))
    # should print True
    s = 'car'
    t = 'rat'
    print(isAnagram(s, t))
    # should print False