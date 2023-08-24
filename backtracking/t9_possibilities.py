"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order."""

def letterCombinations(self, digits: str) -> list[str]:
    if len(digits) == 0:
        return[]
    number_let = {}
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    start = 0
    for number in range(2, 7):
        number_let[str(number)] = alphabet[start:start+3]
        start+=3
    number_let["7"] = "pqrs"
    number_let["8"] = "tuv"
    number_let["9"] = "wxyz"
    def backtrack(index, path):
        if index == len(digits):
            result.append(path)
            return
        for letter in number_let[digits[index]]:
            path +=letter
            backtrack(index+1, path)
            path = path[:len(path)-1]
    result = []
    backtrack(0, "")
    return result

        