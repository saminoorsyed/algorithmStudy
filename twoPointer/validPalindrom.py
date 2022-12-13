# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Explanation:
# use list comprehension to create a list without non-alphanumeric characters that are all lower case
# return bool result of the comparison of the forward and reversed list
def isPalindrome(s: str) -> bool:
    string_only = [letter.lower() for letter in s if letter.isalnum()]
    if len(string_only)==2:
        return string_only[0]==string_only[1]
    half = len(string_only)//2
    return (string_only[:half] == string_only[:half:-1])






if __name__ == '__main__':
    palindrome = "aa"
    print(isPalindrome(palindrome))