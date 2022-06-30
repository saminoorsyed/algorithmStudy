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
        memo = [0]*(change+1)
    # if there is no change left to be made, the recursive call returns 0 [base case]
    if change == 0: 
        return 0
    if memo[change]:
        # this step prevents us from recalculating previously calculated calls is performed at O(1) time
        result = memo[change]
        return memo[change]
    result = change +1
    for i in range(len(denominations)-1):
        # recursively call the function on the new change amount
        if denominations[i] <= change:
            result = min(top_down_make_min_change(change - denominations[i], denominations, memo)+1, result)
            if result < memo[change]:
                memo[change] = result
    return result

def bottom_up_make_min_change(change: int, denominations: list)->int:
    """
    bottom up approach for make change function solves the base case of 0 change first, then iterates up to the change amount
    """
    change_solutions= [change+1]*(change+1)

    for amount in range(1, change + 1):
        for coin in denominations:
            if (coin <= change and (amount - coin))>=0:
                change_solutions[amount] = min(change_solutions[amount], change_solutions[amount - coin]+1)
    if change_solutions[change] > change:
        result = -1
    else:
        result = change_solutions[change]
    return result
    
# naive longest subsequence problem time complexity O(2^n)
def longest_sub_seq(list1, list2):
    """
    find the longest subsequence through dynamic top-down approach
    """
    #base casea
    i = len(list1)
    j = len(list2)

    if i == 0 or j == 0:
        return 0
    if list1[0] == list2[0]:
        count = max(longest_sub_seq(list1[1:], list2)+1, longest_sub_seq(list1, list2[1:])+1)
        return count
    else:
        count = max(longest_sub_seq(list1[1:], list2), longest_sub_seq(list1, list2[1:]))
        return count

    
def bottom_up_lss(list1, list2):
    """
    implement a dynamically programmed bottom up solution to the longest subsequence problem
    """

if __name__ == '__main__':
    # change = 30
    # denominations = [5,8,12,15]

    # print(make_min_change(change, denominations))

    # print(top_down_make_min_change(change, denominations))

    # print(bottom_up_make_min_change(change, denominations))

    list1 = [1]
    list2 = [1]
    print(longest_sub_seq(list1, list2))