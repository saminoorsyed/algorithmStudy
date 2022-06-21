#file that contains Dynamic programming exercises


# Make change Brute force, cannot use conditionals with larger denominations first because it may yield incorrect results

def make_min_change(change: int, denominations: list) -> list:
    """
    function that takes an amount of change and a list of the denominations that can be used to make the change for that amount.

    function will return the fewest number of denominations that will add up to the initial amount(

    # pseudocode:

    if change == 0: return 0
    result = change +1
    for i in range (len(denominations)-1):
        if denominations[i]<= change:
            result = min(make_min_change(change - denominations[i]+1, denominations))
    return result


    param:
    return
    """
    if change == 0: return 0
    # result tracks the number of coins used
    result = change+1
    for i in range (len(denominations)-1):
        if denominations[i] <= change:
            #every recursive call increases the result by one
            result = min(make_min_change(change - denominations[i], denominations)+1, result)
    
    return result


def top_down_make_min_change(change: int, denominations: list, memo: list = [])-> int:
    """
    using a top down approach, we can minimize the amount of work that needs to be done.

    in this case, we can discontinue the recalculation of combinations of coins that have already been solved for by keeping track of what we have already solve through memoization
    """
    # If memo is an empty list, create a list of length change so that a value can be stored at each index. The index represents the value of the remaining change and the value stored is the solution for that change 
    if not memo:
        memo = [None]*(change+1)
    # if there is no change left to be made, the recursive call returns 0 [base case]
    if change == 0: 
        return 0
    if memo[change]:
        # this step prevents us from recalculating previously calculated calls is performed at O(1) time
        result = memo[change]
        return memo[change]
    for i in range(len(denominations)-1):
        # recursively call the function on the new change amount
        if denominations[i] <= change:
            result = min(top_down_make_min_change(change - denominations[i], denominations, memo)+1)
            memo[change] = result
        else:
            result = -1
    return result



if __name__ == '__main__':
    change = 104
    denominations = [5,8,12,15]

    print(make_min_change(change, denominations))

    change = 44
    denominations = [10]
    print(top_down_make_min_change(change, denominations))