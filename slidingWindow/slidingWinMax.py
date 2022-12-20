# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# return the max element from each sliding window possible in the list

# Intuition
# we have to look of an O(n) time solution since we're looking at processing an array. I imagined how I would solve this problem if I could only see the window size, checking the new item against previous maximums as the window moved up the array. this led me to my solution

# Approach
# Here as the window slides from left to right, we start a queue, appending new items to the end of the line, and if any of those items is less than the current item being assessed, we remove it from the end of the line so that the larger item can move forward in the queue. we must also ensure that the item at the front of the queue is the largest item in the window. hence we have a second while statment before adding an element to our final

# Complexity
# Time complexity:
# O(n)

# Space complexity:
# O(n) since the space required to store the answer is directly proportional to the length of the input queue

from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:

    # Initialize an empty monotonic queue
    queue = deque()
    final = []
    # Iterate through the array
    for i, x in enumerate(nums):
        

        # While the queue is not empty and the element at the back of the queue is less than the current element,
        # remove the element at the back of the queue
        while queue and queue[-1][0] < x:
            queue.pop()
        # store a tuple of an element and its index in the que
        queue.append((x,i))

        # while the first item in the queue is outside of the sliding window, remove it
        while i-queue[0][1] >= k:
            queue.popleft()

        # If the queue is of size k, the maximum element is at the front of the queue
        if i >= k-1:
            final.append(queue[0][0])
    return final


# Example usage
print(maxSlidingWindow([7,2,4], 2))



if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print('next')
    print(maxSlidingWindow(nums,k))
#     Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
