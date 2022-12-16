# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# Approach
# since our goal is to find out whether S2 contains a permutation of S1, we should make a hash dictionary
# of each character of S1 where each of its characters is a key and that characters frequency is the value
# after we've created the dictionary , we can iterate through S2 and decriment values in the dictionary
# each time we come across it. once the dictionary is empty that means there is a permutation of S1 in S2

def checkInclusion(s1: str, s2: str) -> bool:
    # build a dictionary of s1 characters and frequencies
    s1Freq = {}
    for char in s1:
        if char not in s1Freq:
            s1Freq[char] = 0
        s1Freq[char]+=1
    # push a window through each item in S2 until s1 is empty
    left = 0
    for right in range(len(s2)):
        # decrement the count of a character if it is encountered by the lead pointer
        # if it did not exist in s1freq, decrement it by 1
        leadChar = s2[right]
        s1Freq[leadChar] = s1Freq.get(leadChar,0)-1
        if s1Freq[leadChar] == 0:
            del s1Freq[leadChar]
        #once the sliding window is the length of s1, add the element that has just slipped out of the window
        # to the frequency count
        if right >= len(s1):
            trailChar = s2[left]
            s1Freq[trailChar] = s1Freq.get(trailChar,0)+1
            left+=1
            if s1Freq[trailChar] == 0:
                del s1Freq[trailChar]
        #remove those characters whose count is 0
        if len(s1Freq) == 0:
            return True
    return False


if __name__ == "__main__":
    s1 = "hello"
    s2 = "ooolleoooleh"

    print(checkInclusion(s1,s2))

# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
