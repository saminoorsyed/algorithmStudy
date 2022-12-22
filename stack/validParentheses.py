# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(self, s: str) -> bool:
    check_vals = {
    "}":"{",
    ")":"(",
    "]": "["
    }
    stack  = []
    for char in s:
        if char in "{([":
            stack.append(char)
        else:
            if len(stack)==0 or stack.pop()!= check_vals[char]:
                return False
    return True if len(stack)==0 else False


if __name__ == "__main__":
    
    t1 = "()" #true
    t2 = "()[]{}" #true
    t3 = "{]" #false

    print(isValid(t1))
    print(isValid(t2))
    print(isValid(t3))