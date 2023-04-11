# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# here build from left to right, only adding ')' when one more open parenthesis exists than a closed parenthesis
def generateParenthesis(n):
        # here open and closed rep the number of each type of parenthesis we can have
        def recursion(perm, open, close, permutations=[]):
            # if we haven't used up all of our open parenthesis
            if open:         
                recursion(perm + '(', open-1, close)
            # only add closed parenthesis if there is a matching open parenthesis
            if close > open: 
                recursion(perm + ')', open, close-1)
            if not close:
                    permutations.append(perm),
            return permutations
        return recursion('', n, n)


# not a great solution, generates all possible iterations instead of just the ones that work
# def generateParenthesis(n: int)->list[str]:
#     return generateParenthesisHelper(n, "", [])
# def generateParenthesisHelper(n: int, permutation: str = "", final: list =[]) -> list[str]:
#     def isValid(permutation):
#         stack =[]
#         for char in permutation:
#             if char == "(":
#                 stack.append(char)
#             else:
#                 if len(stack)==0 or stack.pop() != "(":
#                     return False
#         return True if len(stack)==0 else False
#     if len(permutation) >= 2*n:
#         if permutation not in final and isValid(permutation):
#             final.append(permutation)
#         return
#     permutation += '('
#     generateParenthesisHelper(n, permutation, final)
#     permutation = permutation[:-1]
#     permutation +=')'
#     generateParenthesisHelper(n, permutation, final)

#     return final


# helper function to determine whether parenthesis set is true
# def isValid(permutation):
#     stack =[]
#     for char in permutation:
#         if char == '(':
#             stack.append('(')
#         elif char == ')':
#             if len(stack) == 0 or stack.pop()!='(':
#                 return False
#     return True


if __name__ == "__main__":
    n = 3
    print(generateParenthesis(n))
    # Output: ["((()))","(()())","(())()","()(())","()()()"]
    n=1
    print(generateParenthesis(n))

    # Output: ["()"]