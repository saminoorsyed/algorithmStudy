# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# explanation:
# first we turn the list into a set so that we can query it in O(1) time
# then for each element in the array, we check if we are at the end of a streak, if not, we skip over it
# if we are, then we check each smaller element iteratively until we reach the end of the consecutive streak
# the difference between the last and first element of the streak is the streaks length. Use max compare with 
# previous steaks.

def longestConsecutive(nums: list[int]) -> int:
    nums = set(nums)
    longest = 0
    for el in nums:
        if el + 1 not in nums:
            next_num = el-1
            while next_num in nums:
                next_num -=1
            longest = max(longest, el - next_num)
    return longest
        


if __name__ == '__main__':

    nums = [8,0,3,7,2,5,4,6,0,1]
    print(longestConsecutive(nums))
    # should return 4 b/c 1,2,3,4


#intuition
# since the algo has to run in O(n) time and seemingly access non-sequential elements in the array, we likely have to use a hash
# APPROACH:
# to reduce the number of computations necessary, we can run the built in set() function on the array. That should eliminate the 
# duplicates in that array and run in O(n) time
# from there we can create a hash of the array using numbers as keys, and log the lowest and highest number. then we iterate through
# a consecutive list and check each consecutive value, incrementing the counter when it is in the hash table and resetting it when it
# is not. From there we can track a longest variable and update it whenever a longer consecutive streak is found 
# EDGE case:
#  if the list has a length of 0

# def longestConsecutive(nums: list[int]) -> int:
#     # edge case: if nothing is in the list, return 0
#     if len(nums) == 0:
#         return 0
#     # create a hash using a dictionary of the array elements as keys. each val = 1 (this takes O(n) time)
#     num_dict = {}
#     for el in nums:
#         if el not in num_dict:
#             num_dict[el] = 1
#     # create a list of the values in the numbers dict
#     num_set = list(num_dict.keys())
#     # start building the longest sequence by iterating through each item in the list
#     for el in num_set:
#         consec = el
#         # prevent from checking values that have already been counted in a consecutive list
#         if num_dict[consec] !=1:
#             continue
#         # loop through each decreasing number, adjusting the current element to reflect how many consecutive numbers have been found
#         # the while conditional runs in )(1) time and the loop takes at most n iterations 
#         while consec - 1 in num_set:
#             # if we run into a previously calculated sequence, add it to the current total and discontinue the loop
#             if num_dict[consec-1]!= 1:
#                 num_dict[el] += num_dict[consec-1]
#                 break
#             #  update the count of the original number
#             num_dict[el]+=1
#             #  mark each consecutive integer found so that it is not checked on future iterations in the for loop
#             num_dict[consec]= 2
#             # check the next consecutive integer
#             consec-=1

#     return max(list(num_dict.values()))