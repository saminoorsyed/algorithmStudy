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

# bottom up approach of longest subsequence problem time complexity is O(m+n) where m and n are the lengths of m and n
def bottom_up_lss(list1, list2):
    """
    Implement a dynamically programmed bottom up solution to the longest subsequence problem
    """

    # create a two dimensional array to represent all of the solutions
    m = len(list1)
    n = len(list2)
    columns = [0]*m+1
    subsol = [columns] * n+1
    for row in n:
        for column in m:
            if m == 0 and n == 0:
                subsol[row][column] = 0
            elif list1[row] == list2[column]:
                subsol[row][column] = subsol[row-1][column-1] +1
            else:
                subsol[row][column] = max(subsol[row-1][column], subsol[row][column-1])
    return subsol[n][m]

def knapsack_unbounded(weights:list, values:list, capacity: int)-> int:
    """
    Computes the highest value solution for a nap sack of a specified capacity given the weights and values of the items that would fit into it. Outputs the maximum value
    """

    cache = [0]* (capacity+1)

    for x in range(1,capacity+1):
        for i in range (len(weights)):
            wi = weights[i]
            if wi <= x:
                cache[x] = max(cache[x], cache[x-wi] + values[i])
    return cache[len(weights)]

def knapsack_01(weights:list, values:list, capacity:int, cache:list = [])-> int:
    """
    computes the optimal solution for a nap sakc of specified capacity given that each item can only be chosen once
    """
    if capacity == 0 or len(weights) == 0:
        return 0
    cache = [[0]*(len(weights))] * (capacity+1)
    if capacity == 0 or len(weights) == 0:
        return 0
    for x in range(capacity+1):
        for i in range(len(weights)):
            wi = weights[i]
            if capacity == 0:
                cache[x][i] = 0
            elif wi <= x:
                cache[x][i]= max(cache[x-wi][i-1] + values[i], cache[x][i-1])
    return cache[capacity][len(weights)-1]



if __name__ == '__main__':
    weights = [1,2,3,4]
    values = [10,20,5,15]
    print(knapsack_unbounded(weights,values,10))
    print(knapsack_01(weights,values,10))