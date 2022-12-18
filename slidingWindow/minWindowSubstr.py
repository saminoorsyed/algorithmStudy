# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring of s such that every character in t (including duplicates) is included in 
# the window. If there is no such substring, return the empty string "". The testcases will be generated such that the answer is unique.

# Approach:
# Here we can use a similar approach by creating a window that expands from the left to the right and checks a dictionary that contains the
# frequency of each element needed to be found
def minWindow(s: str, t: str) -> str:
    # create a dictionary of the search string
    search_dict = {}
    for el in t:
        search_dict[el] = search_dict.get(el, 0)+1
    # set the pointers for the windows and set the longest == to one more than the length of the string
    # this way if the search string exists in the full length, we can return the whole string. if not,
    # the min will be greater than the length of the string. If contains is set, the window contains the
    # search string, if it is cleared, it does not.
    left = 0
    right = 0
    minimum = len(s)+1
    contains = len(search_dict)
    answer = ""
    # loop until the space between the left pointer and the end can no longer encompass the search list
    while right< len(s):
        # if the character is in the search checker, decrement it's value in the dict by one
        if s[right] in search_dict:
            search_dict[s[right]] -= 1
            if search_dict[s[right]] == 0:
                contains -=1
            
        #loop to move the left side of the window up as long as the window contains the search
        while contains <= 0:
            if right-left+1 < minimum and contains <= 0:
                minimum = right-left+1
                answer = s[left:right+1]
            if s[left] in search_dict:
                search_dict[s[left]]+=1
                if search_dict[s[left]]==1:
                    contains+=1
                # if if the search string is still contained and the window is less than the minimum, adjust the answer
                elif right-left < minimum:
                    minimum = right-left
                    answer = s[left+1:right+1]
            left +=1
        right+=1
    return answer
        
        

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s,t))
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.