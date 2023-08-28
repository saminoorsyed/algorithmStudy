def longestCommonPrefix( strs: list[str]) -> str:
    longest = len(strs[0])
    common = strs[0]
    for word in strs:
        count = 0
        index = 0
        while index < longest:
            if index < len(word) and word[index] == common[index]:
                count +=1
            else:
                break
            index +=1
        if count < longest:
            longest = count
            common = word[0:index]
    return common

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(strs))
    strs = ["a"]
    print(longestCommonPrefix(strs))