# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# APPROACH:
# Here we move our sliding window from left to right, using the max_freq + k as criteria for when to move our left pointer to the right
# if that criteria is greater than the difference between the pointers, we need to move the left pointer and decrement the val of what
# it points to.
def characterReplacement(s: str, k: int) -> int:
    freq = {}
    max_freq = 0
    start = 0
    longest = 0

    for end in range(len(s)):
        freq[s[end]] = freq.get(s[end], 0) + 1

        max_freq = max(max_freq, freq[s[end]])

        diff = (end - start + 1 - (max_freq + k))

        if diff > 0:
            freq[s[start]] -= 1
            start += 1

        longest = end - start + 1

    return longest

if __name__ == "__main__":
    s = "ABAB"
    k = 2
    print(characterReplacement(s, k))
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

    s = "ABBBBAAAB"
    k = 1
    print(characterReplacement(s, k))
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.



# APPROACH:
# Here we us a binary search function in conjunction with a log of the most frequently occuring character to obtain the longest substring.
# initially the minimum length substring will be set to 1, and the max will be set to the length of the string. from there, we will check
# if the middle length or "target length" substring exists in the original list using a sliding window. to do so, we will iterate, the
# right pointer until the window length is equal to the target length and then the left pointer will move along with the right pointer.
# to check if the target length contains a vaild substring, we will track the most common character. If the frequency of the most common
# character + k adds up to the target length, then there is a valid string and we look for a larger target value, setting the new min to 
# middle+1 and then the new middle to (min+1+hi)//2. if there is not a vaild string, we check for a shorter target length by adjusting the
# hi valid string to be middle -1. and finding a new middle between the low and new hi

# def characterReplacement(s: str, k: int) -> int:
#     # set up binary search pointers
#     low = 1
#     hi = len(s)
#     longest = low
#     # function to determine if a valid sub string of the target length exists within the string
#     def is_valid(target_length):
#         #set up pointers and dictionary for left and right of the window
#         left, right = 0, 0
#         frequency = {}
#         maximum = 1
        
#         # while loop to create the window and track frequencies and check validity
#         while right< len(s):
            
#             # track the leading edge of the frequencies
#             if s[right] not in frequency:
#                 frequency[s[right]] = 0
#             frequency[s[right]] += 1
            
#             # the window length == the target length, start decrementing characters from the left pointer 
#             if right >= target_length:
#                 frequency[s[left]] -= 1
#                 left +=1
            
#             # set the maximum = to the character that shows up the most
#             maximum = max(frequency[s[right]], maximum)
            
#             # check if there is a valid array
#             if maximum + k >= target_length:
#                 return True
            
#             right +=1
#         return False

#     # the outer loop should be a binary search algorithm
#     while low <= hi:
#         middle = (low+hi)//2
#         if is_valid(middle):
#             low = middle+1
#             longest = middle
#         else:
#             hi = middle-1

#     return longest

























# def characterReplacement(s: str, k: int) -> int:
#     # edge case
#     if len(s)<1:
#         return 0
#     left = 0
#     right = 1
#     longest = 1
#     kCount = k
#     starter = 0
#     # consider the case in which the first letter is different to a long repeating string
#     if s[left]!=s[right] and kCount>0:
#         kCount -=1
#         longest = 2
#         left+=2
#         while s[right] == s[left] or kCount>0:
#             if s[right]!= s[left]:
#                 kCount-=1
#             left +=1
#             longest+=1
#             if left>= len(s):
#                 break

#     left = 0
#     right = 1
#     kCount = k
#     while right < len(s):
#         # if the letter at the right pointer is not the same as the letter at the right pointer use a kCount to increment 
#         # to the next value. if there are no more kCounts, push the pointer back to the starter index
#         if s[right] != s[left]:
#             # track the first different letter
#             if kCount == k:
#                 starter= right
#             # if the list cannot be extended again, move the left pointer to the starter position and the right pointer to one place after that, reset kCount start the count again
#             if kCount == 0:
#                 left = starter
#                 right = starter+1
#                 kCount = k
#                 continue
#             # decrement the kCount to represent adjusting on of the letters
#             kCount-=1
#         # if the difference inclusive between the left and right pointer is greater than the longest, replace the longest
#         difference = right - left+1
#         if difference > longest:
#             longest = difference
        
#         right += 1
#     return longest