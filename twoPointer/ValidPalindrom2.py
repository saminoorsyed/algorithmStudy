# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def validPalindrome(s: str) -> bool:
    low = 0
    high = len(s)-1
    while low<=high:
        if s[low]==s[high]:
            low +=1
            high-=1
        else:
            print(low-1)
            print(s[high-1:low:-1]+s[low])
            print(s[low:high])
            return s[low+1:high+1]==s[high:low:-1] or s[low:high]==(s[high-1:low:-1]+s[low])
    return True
        

if __name__ == "__main__":

# Example 1:

    s = "aba"
    print(validPalindrome(s))
# Output: true
# Example 2:

    s = "abca"
    print(validPalindrome(s))

# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

    s = "abc"
    print(validPalindrome(s))

# Output: false

# Example 4:
    s ="eccer"
    print(validPalindrome(s))