def longestPalindrome(s: str) -> str:
    if s == s[::-1]:
        return s
    size = 1
    start = 0
    for i in range(1, len(s)):
        l,r = i-size, i+1
        s_odd = s[l-1:r]
        if l>=1 and s_odd == s_odd[::-1]:
            size +=2
            start = l-1
        else:
            s_even = s[l:r]
            if s_even == s_even[::-1]:
                size += 1
                start = l
    return s[start: start+size]


if __name__ == "__main__":
    s = "10123456789"
    print(longestPalindrome(s))