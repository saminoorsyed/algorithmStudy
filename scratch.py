def valid_parenthesis(input_str: str)-> bool:
    stack = []
    valid_dict = {
            "(":")" ,
            "[": "]",
            "{": "}",
            "<": ">",
            }

    for el in input_str:
        if el in valid_dict.keys():
            stack.append(valid_dict[el])
        elif el in valid_dict.values():
            if stack and stack.pop() == el:
                continue
            else: 
                return False
    return True if len(stack) == 0 else False


if __name__ == "__main__":
    input_str = ")))"
    print(valid_parenthesis(input_str))
