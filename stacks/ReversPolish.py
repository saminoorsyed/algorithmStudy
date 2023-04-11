# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

def evalRPN(tokens: list[str]) -> int:
    stack = []
    operators=('+','-','*','/')
    result = None
    if len(tokens) == 1:
        # type should match other outputs
        return int(tokens[0])
    for item in tokens:
        if item in operators:
            operand2 = stack.pop()
            result = stack.pop()
            if item == '+':
                result += operand2
            elif item == '-':
                result -= operand2g
            elif item == '*':
                result *= operand2
            elif item == '/':
                result= int(result / operand2)
                # result = result//operand2
                # floor divided only rounds down, int will truncate numbers
            
            stack.append(result)

        else:
            newInt = int(item)
            stack.append(newInt)
    return result


if __name__ == "__main__":
    tokens = ["2","1","+","3","*"]
    print(evalRPN(tokens))

# Output: 9
# Explanation: ((2 + 1) * 3) = 9
    tokens = ["4","13","5","/","+"]
    print(evalRPN(tokens))
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens))
# Output: 22
# Explanation: we're getting 12 because it needs to truncate toward 0, and when we divide 6 by -132 we should get 0 not -1,

    tokens = ["18"]
    print(type(evalRPN(tokens)))

# Output: int
# Explanation: edge case of a tokens only having a length of 1