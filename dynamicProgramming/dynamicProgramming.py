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
    result = None
    if change == 0: return 0
    # result tracks the number of coins used
    result = change+1
    for i in range (len(denominations)-1):
        if denominations[i] <= change:
            #every recursive call increases the result by one
            result = min(make_min_change(change - denominations[i], denominations)+1, result)
    
    return result

if __name__ == '__main__':
    change = 35
    denominations = [10,7,5,1]

    print(make_min_change(change, denominations))