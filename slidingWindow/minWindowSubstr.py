# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring of s such that every character in t (including duplicates) is included in 
# the window. If there is no such substring, return the empty string "". The testcases will be generated such that the answer is unique.

def minWindow(self, s: str, t: str) -> str:

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s))
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.