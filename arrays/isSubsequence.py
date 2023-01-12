# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


def isSubsequence(s: str, t: str) -> bool:
    searcher = 0
    searched = 0
    starter = s[searcher]
    # end the loop when all elements of the first list have been found
    while searcher < len(s):
        # once each of the elements has been searched in the second list
        if searched >= len(t):
            return False
        # if the elements are equal, increment both indexes
        if t[searched] == s[searcher]:
            searched+=1
            searcher+=1
        else:
            searched+=1
    return True

if __name__ =="__main__":
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s,t))
# Output: true
    s = "axc"
    t = "ahbgdc"
    print(isSubsequence(s,t))

# Output: false