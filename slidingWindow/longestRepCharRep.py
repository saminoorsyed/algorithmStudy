# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# APPROACH:
# Here we have to employ a check as you go mentality, looking for the longest character string possible from the start. 
# once that is achieved with what is given, we look for the next longest repeating character string

def characterReplacement(s: str, k: int) -> int:
    # edge case
    if len(s)<1:
        return 0
    left = 0
    right = 1
    longest = 1
    kCount = k
    starter = 0
    # consider the case in which the first letter is different to a long repeating string
    if s[left]!=s[right]:
        kCount -=1
        left+=1
        right+=1
    while right < len(s):
        # if the letter at the right pointer is not the same as the letter at the right pointer use a kCount to increment 
        # to the next value. if there are no more kCounts, push the pointer back to the starter index
        if s[right] != s[left]:
            # track the first different letter
            if kCount == k:
                starter= right
            # if the list cannot be extended again, move the left pointer to the starter position and the right pointer to one place after that, reset kCount start the count again
            if kCount == 0:
                left = starter
                right = starter+1
                kCount = k
                continue
            # decrement the kCount to represent adjusting on of the letters
            kCount-=1
        # if the difference inclusive between the left and right pointer is greater than the longest, replace the longest
        difference = right - left+1
        if difference > longest:
            longest = difference
        
        right += 1
    return longest
        

if __name__ == "__main__":
    s = "ABAB"
    k = 2
    print(characterReplacement(s, k))
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

    s = "AABABBA"
    k = 1
    print(characterReplacement(s, k))
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.