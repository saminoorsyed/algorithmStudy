# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# APPROACH:
# in this case we are looking for the greatest difference between two points where the first point is the lowest and the second is the highest
# here we can track the max profit by iterating the right pointer right at each iteration. if the right pointer is below the left pointer we set 
# the left pointer to the right pointer and increment the right pointer by one. this should work, because the largest profit after a point should 
# have the lowest buy value after said point. there can be a higher profit recorded before that point

def maxProfit(prices: list[int]) -> int:
    # edge case if there is 1 or fewer elements:
    if len(prices) < 2:
        return 0
    # Set pointers to the first and second value of the list and profit to 0 (hopefully the worst case)
    left = 0
    profit = 0
    #iterate through each item until the right pointer reaches the end
    for right in range(1,len(prices)-1):
        #replace profit if a greater value is found
        difference = prices[right]-prices[left]
        if difference>profit:
            profit = difference
        # if a lower value than the current left pointer is found, make it the new left pointer
        if prices[left]> prices[right]:
            left = right
        right += 1
    return profit

if __name__ == "__main__":
    prices = [7,6,4,3,1]
    print(maxProfit(prices))
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.