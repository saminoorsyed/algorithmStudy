# check if the number is a palindrome without converting it into a string

def isPalindrome(x: int) -> bool:
    if x <0:
        return False
    number_list = []
    while x!=0:
        num = x % 10
        x = x//10
        number_list.append(num)
    return number_list == number_list[::-1]
