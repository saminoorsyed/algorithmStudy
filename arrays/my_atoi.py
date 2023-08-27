def myAtoi(s: str) -> int:
    s = s.strip()
    is_neg = False
    if s[0] == "-":
        is_neg = True
        s = s[1::]
    if s[0] == "+":
        s = s[1::]
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    for digit in range(len(s)-1):
        if s[digit] not in digits:
            s = s[:digit]
            break
    while s[0] == "0":
        s = s[1::] 
    count = 0
    number = 0
    upper = 2**31
    for i in range(len(s)) :
        number += int(s[i])*(10**(len(s)-count-1))
        count += 1
        if (number > upper):
            if is_neg:
                return -1*(upper) 
            else:
                return upper-1
    return -1 * number if is_neg else number

if __name__ == "__main__":
    s = "    -42"
    print(myAtoi(s))