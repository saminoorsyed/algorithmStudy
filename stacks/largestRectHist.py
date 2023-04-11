# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Approach:
# Here we will iterate from the left to the right, pushing higher heights to a stack along with their index (for the purpose of calculating areas) and then as soon as a lower height value is discovered, we can move back along the stack finding the area of the largest rectangle possible at each height above the new lower height. we must append this new height after moving back through the stack.
#  
def largestRectangleArea( heights: list[int]) -> int:
    stack= []
    area = 0
    for index, height in enumerate(heights):
        # if the new height is greater than the previous height appended to the stack, add the new height and index to the stack
        if not stack or height>stack[-1][1]:
            stack.append((index,height)) 
        # the stack should not be adjusted for heights that are equal
        if height == stack[-1][1]:
            continue
        # when a lower height is found, pop the last values of the stack and find the max area from their
        while stack and height < stack[-1][1]:
            left, h = stack.pop()
            area = max(area, (index-left)*h)
        stack.append((left,height))

    while stack:
        left, height = stack.pop()
        area = max(area, (len(heights)-left)*height)
    
    return area
    
    


if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    print(largestRectangleArea(heights))
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.