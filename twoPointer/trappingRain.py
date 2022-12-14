# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
# Here we still want to calculate the maximum amount of water held, but now we have to subtract out the area taken up by bars within our containers. we can use a similar approach to finding the maximum container

# # Approach
# <!-- Describe your approach to solving the problem. -->
# using the min of the two bars in consideration, you find the max water that can be held between the two. adjust the pointer pointing to the lowest bar. This will ensure that we're adding all the water held. As we run into bars we have to subtract out their area, and if those bars contain water at a higher altitude, we need to add that water to our calculation.
# # Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# O(n), since we only have one iteration throught the list

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# O(1), this solution requires no extra space in proportion to the size of the input list

def trap(height: list[int]) -> int:
    # set initial values for the pointers as well as height examined
    left = 0
    right = len(height)-1
    water = 0
    base_height= 0
    # the loop should continue until the left pointer has caught up with the right pointer at the end of the list
    while left<right:
        #starting from the widest interval, we figure out if water can be held above the previous container
        min_height =  min(height[left], height[right])
        cont_height = min_height-base_height
        # if so, add the total volume to the water
        if cont_height> 0:
            base_height += cont_height
            width = right - left
            water+=cont_height*width
        # adjust the pointers based on trying to find the max water held and remove water area below the current base height
        if min_height == height[left]:
            #only remove area that is submersed
            if height[left]<base_height:
                water-=height[left]
            else:
                water -= base_height
            left +=1
        else:
            if height[right]<base_height:
                water-=height[right]
            else:
                water -= base_height
            right-=1
    return water
if __name__ == "__main__":
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(heights))

    # Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.