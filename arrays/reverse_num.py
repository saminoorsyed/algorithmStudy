"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0."""


def reverse(x: int) -> int:
    is_neg = False if x > 0 else True
    x = abs(x)
    x_str = str(x)[::-1]
    neg = 1
    if is_neg:
        neg = -1
    final = int(x_str)*neg
    b = final.bit_length ()
    if (b > 31 and x >= 0) or (b > 31 and x < 0): return 0
    return final