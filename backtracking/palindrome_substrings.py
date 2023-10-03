def partition(s: str) -> list[list[str]]:
    def is_pal(letters:str)->bool:
        return letters == letters[::-1]
    
    def backtrack(start:int, path: str):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start +1, len(s)+1):
            if is_pal(s[start:end]):
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()

    result = []
    backtrack(0, [])
    return result

if __name__ == "__main__":
    s = "aabaa"
    print(partition(s))