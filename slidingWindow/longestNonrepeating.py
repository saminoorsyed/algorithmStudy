# Given a string s, find the length of the longest substring without repeating characters.
#APPROACH:
# here we use a left pointer and a right pointer starting consecutively. upon each iteration, the right pointer increments
# and checks a hash of strings that it has passed. if it duplicates one of those values, the left pointer must iterate just
# past that value, removing those keys from the dictionary as it goes 
def lengthOfLongestSubstring(s: str) -> int:
    #edge case
    if len(s)<1:
        return 0
    #initiate the pointers and add their values to the dictionary
    left = 0
    longest = 1
    dupCheck = {
        s[left] : 0
        }
    for right in range(1, len(s)):
        if s[right] in dupCheck:
            # set double to the index value of the duplicated character
            double = dupCheck[s[right]]
            # delete all keys in the dictionary that are before the duplicated character
            while left <= double:
                del dupCheck[s[left]]
                left +=1
        # set the value of the current character to its index value
        dupCheck[s[right]]= right
        # check the difference (inclusive) and replace longest if needed
        difference = right - left+1
        if difference> longest:
            longest = difference

    return longest


if __name__ == "__main__":
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))
    # Output: 3
    # Explanation: The answer is "abc", with the length of 3.
    s = "abcaasdfkjanoalkajnapivnaweviwnaqwertyuiopasdfghjklzxcvbnm"
    print(lengthOfLongestSubstring(s))
    s = "aaaaaaaaaaaaa"
    print(lengthOfLongestSubstring(s))