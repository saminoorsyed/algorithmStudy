# Given a string s consisting of words and spaces, return the length of the last word in the string.
def lengthOfLastWord(s: str) -> int:
    end = len(s)-1
    count = 0
    while s[end] == " ":
        end-=1
    while s[end]!= " " and end>=0:
        count+=1
        end-=1
    return count

if __name__ =="__main__":
    s = "Hello World"
    print(lengthOfLastWord(s))
# Output: 5
# Explanation: The last word is "World" with length 5.
    s = "   fly me   to   the moon  "
    print(lengthOfLastWord(s))
# Output: 4
# Explanation: The last word is "moon" with length 4.
    s = "luffy is still joyboy"
    print(lengthOfLastWord(s))
# Output: 6
# Explanation: The last word is "joyboy" with length 6.