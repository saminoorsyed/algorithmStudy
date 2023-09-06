# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
def remove_k(num:str, k: int)-> str:
    num_stack = []
    for el in num:
        while k and num_stack and el < num_stack[-1]:
            num_stack.pop()
            k -=1
        num_stack.append(el)
    final = num_stack[:-k] if k else num_stack
    return "".join(final).lstrip('0') or '0'

if __name__ == "__main__":
    num = "1432219"
    k = 3
    print(remove_k(num,k))