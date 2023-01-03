# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour. Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.Return the minimum integer k such that she can eat all the bananas within h hours.

# Approach:
#  here we do a binary search not of the piles, but of the values between the max of the piles and the minimum. the criteria through which we choose to adjust the hi and low values is whether the hours to eat the piles of bananas in the current time is greater than the hours alloted to Koko. if it is, we increase the minimum to the middle value, which should move the middle value up (the value which is used to asses whether the Bananas can be eaten in time). 

# The time complexity of this solution is O(Nlog(max(Piles)))


def minEatingSpeed(piles: list[int], h: int) -> int:
    low, hi = 1, max(piles)
    while low < hi:
        middle = (low + hi) // 2
        # Here, we did not have enough time to eat the bananas so we have to increase the middle number
        if sum((pile + middle - 1) // middle for pile in piles) > h:
            low = middle + 1
        # Here, we had time to spare, so we can reduce the middle number 
        else:
            hi = middle
    return low

if __name__ == "__main__":
    piles = [3,6,7,11]
    h = 8
    print(minEatingSpeed(piles, h) )
# Output: 4
    piles = [30,11,23,4,20]
    h = 5
    print(minEatingSpeed(piles, h) )
# Output: 30
    piles = [30,11,23,4,20]
    h = 6
    print(minEatingSpeed(piles, h) )
# Output: 23