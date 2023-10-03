def convert(s: str, numRows: int) -> str:
    if numRows > len(s)-1 or numRows ==1:
            return s
    mod = numRows + numRows-2
    rows = ["" for i in range(numRows)]
    for i in range(len(s)):
        place = i % mod
        if place < numRows:
            rows[place]+=s[i]
        else:
            place  = mod - (i%mod)
            rows[place]+= s[i]
    result = ""
    for row in rows:
        result += row
    return result

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    n = 3
    print(convert(s, 4))