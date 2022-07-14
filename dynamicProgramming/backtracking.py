def makechange_bottomup(coins, amount):

    min_count_table = [amount+1]*(amount+1) # setting array elements to some large value that is not possible answer

    min_count_table[0] = 0 # setting the base case

    coins_used = [0 for coin in range(amount+1)]

    for i in range(1, amount+1):  # iterate through all possible amount values from base case
        for j in range(0, len(coins)): #find the number of coins needed for each coin denomination
            coin_val = coins[j]
            if(coin_val <= amount): # if denomination value is less than amount then we can use the coin
                # replace min_count_table[i] with minumum value of coins possible
                if (min_count_table[i] > min_count_table[i-coin_val]+1):
                    coins_used[i] = coin_val
                    min_count_table[i] = min_count_table[i-coin_val]+1

    result=[]
    # we have a valid count of coins if min_count_table[amount] is valid
    if min_count_table[amount] > amount: result = -1
    else:
        while amount>0:
            result.append(coins_used[amount])
            amount = amount - coins_used[amount]

    return  result

def LCS_backtrack(list1: list, list2: list) -> list:
    """
    bottom up solution to longest common subsequence problem with backtracking
    """
    # cache = [[0 for x in range(n+1)] for x in range(m+1)]
    cache = [[0 for x in range(len(list1)+1)] for x in range(len(list2)+1)]
    for row in range(len(list2)+1):
        for column in range(len(list1)+1):
            if row == 0 or column == 0:
                cache[row][column] = 0
            elif list1[column-1] == list2[row-1]:
                cache[row][column] = cache[row-1][column-1]+1
            else:
                cache[row][column] = max(cache[row-1][column], cache[row][column-1])
    count = 0
    length1 = len(list1)
    length2 = len(list2)
    solution = []
    while count < cache[len(list2)][len(list1)]:
        if list1[length1-1] == list2[length2-1]:
            solution.append(list1[length1-1])
            length1 -= 1
            length2 -= 1
            count+=1
        elif cache[length2][length1] == cache[length2][length1-1]:
            length1 -=1
        else:
            
            length2 -= 1
    solution.reverse()
    return solution

if __name__ == '__main__':
    list1 = [1,6,3,4,5]
    list2 = [1,2,3,4]

def knapsack_unbounded(weights:list, values:list, capacity: int)-> int:
    """
    Computes the highest value solution for a nap sack of a specified capacity given the weights and values of the items that would fit into it. Outputs the maximum value
    """

    cache = [0]* (capacity+1)
    items_used = [0 for item in range(capacity+1)]
    for x in range(1,capacity+1):
        for i in range (len(weights)):
            wi = weights[i]
            if wi <= x:
                if cache[x] < cache[x-wi] + values[i]:
                    items_used[x] = i
                    cache[x] = cache[x-wi] + values[i]
    items = []
    while capacity > 0:
        items.append(items_used[capacity])
        capacity = capacity- weights[items_used[capacity]]

    return items

if __name__ == '__main__':
    weights = [4, 9, 3, 5, 7]
    values = [10, 25, 13, 20, 8]
    print(knapsack_unbounded(weights,values,10))
    print(makechange_bottomup([1,3,5],8))