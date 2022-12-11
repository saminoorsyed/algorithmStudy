# INTUITION:
# as we loop through the array, we must search for the remaining amount to add to the sum. 
# Approach:
# Instead of iterating through it a second time for each value needed to be checked, we can implement a dictionary to track the items 
# we have already found using the elements as keys to store their index value allows us to use the dictionary as we might a hash map,
# resulting in an added cost of O(1) time. looping through the list of numbers as it exists gives O(n) time complexity



def twoSum(nums: list[int], target: int)-> list[int]:
    """
    creates a dictionary with key:value = element: index as it iterates through
    once the required difference is found, the loop terminates
    """

    differences = {}

    for index, element in enumerate(nums):
        # set the key = to the difference fo the target and the current item
        key = target - element
        # the 'in' operator here has a time complexity of O(1) assuming a good hash because it is being applied to a dictionary
        if key in differences:
            return index, differences[key]
        differences[element] = index

if __name__ == '__main__':
    
    num_array = [2,11,35,7,8]
    target = 9
    print('hello')
    print(twoSum(num_array, target))