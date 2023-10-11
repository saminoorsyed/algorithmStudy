def rod_cutting(prices:list[int], length:int)->int:
    memo = [-1]*(length+1)
    memo[0] = 0
    rod_cutting_helper(prices, length, memo)
    return memo[length]

def rod_cutting_helper(prices:list[int], length:int, memo)->int:
    """ find the maximum value for cutting a rod into different lengths given an array of prices"""
    # if the sub problem has already been solved, return the solution
    if memo[length] != -1:
        return memo[length]
    max_val = -1
    for sol in range(1, length +1):
            max_val = max(max_val, prices[sol-1] + rod_cutting_helper(prices, length-sol, memo))
    memo[length] = max_val

    return max_val

prices = [1,3,5,6,0,0,0,0,0,0,0,0,0,0,0]
length = 11
print(rod_cutting(prices, length))