# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# APPROACH:
# Since we are looking for the max area, we know that as we adjust our system we should continue attempting to increase our area. Since we are looking to maximize both width and height, or rather their combination, it is helpful to use a two pointer solution. starting with our pointers at either end of the array, and tracking the difference in indices, we should always move the smaller of the two pointers (height). otherwise we are not not maximizing the area of the next rectangle
def maxArea(height: list[int]) -> int:
    # set pointers to the beg and end of the list and starter area for the loop
    left = 0
    right = len(height)-1
    width = right- left
    m_area = 0
    # loop through each value finding the next highest container area by adjusting the pointer with lesser height
    while width>0:
        #find the area of the current rectangle and compare it to the current m_area
        cont_height = min(height[left], height[right])
        width = right-left
        cont_area = cont_height*width
        #adjust the pointer that has the smaller height value
        if cont_area>m_area:
            m_area = cont_height*width
        if cont_height == height[left]:
            left+=1
        else:
            right-=1
    return m_area





if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
