def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller list
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    
    while low <= high:
        partition_nums1 = (low + high) // 2
        partition_nums2 = (m + n + 1) // 2 - partition_nums1
        
        # Calculate the elements on the left and right side of the partitions
        max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
        min_right_nums1 = float('inf') if partition_nums1 == m else nums1[partition_nums1]
        
        max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
        min_right_nums2 = float('inf') if partition_nums2 == n else nums2[partition_nums2]
        
        # Check if the partitions are correct
        if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
            # Calculate the median based on the total number of elements
            if (m + n) % 2 == 0:
                return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
            else:
                return max(max_left_nums1, max_left_nums2)
        elif max_left_nums1 > min_right_nums2:
            high = partition_nums1 - 1
        else:
            low = partition_nums1 + 1

if __name__ == "__main__":
    # Example 1:

    nums1 = [1, 2, 3, 4, 5, 6, 7]
    nums2 = []
    print("should return 4")
    print(findMedianSortedArrays(nums1, nums2))
    # Example 2:

    print("should return 4")
    nums1 = []
    nums2 = [1, 2, 3, 4, 5, 6, 7]
    print(findMedianSortedArrays(nums1, nums2))

    # Explanation: same as the last test, checking that longer list is assigned list 1 in code

    print("should return 5.5")
    nums1 = [8, 9, 10]
    nums2 = [1, 2, 3, 4, 5, 6, 7]
    print(findMedianSortedArrays(nums1, nums2))

    # Output: 5.5
    # Explanation: check that median is average of 6 and 7
    print("should return 5.5")
    nums1 = [8, 9, 10]
    nums2 = [1, 2, 3]
    print(findMedianSortedArrays(nums1, nums2))

    # Output: 5.5
    # Explanation: median is the average of 3 and 8
    print("should return 7")
    nums1 = [7, 8, 9, 10]
    nums2 = [1, 2, 3]
    print(findMedianSortedArrays(nums1, nums2))

    # Output: 7
    # Explanation: median is in the second list, odd total length
    print("should return 6.5")
    nums1 = [6, 7, 8, 9, 10]
    nums2 = [1, 2, 3]
    print(findMedianSortedArrays(nums1, nums2))

    # Explanation: median is in the second list, even total length

    print("should return 2.5")
    nums1 = [1, 3]
    nums2 = [2, 7]
    print(findMedianSortedArrays(nums1, nums2))

    # Output: 2.5
    # Explanation: median is in the second list, even total length
    print("should return 0")
    nums1 = [0, 0]
    nums2 = [0, 0]
    print(findMedianSortedArrays(nums1, nums2))

    # Output:
    # Explanation: median is in the second list, even total length
    print("should return 1")
    nums1 = [1, 2]
    nums2 = [1, 1]
    print(findMedianSortedArrays(nums1, nums2))

    # Output:
    # Explanation: median is in the second list, even total length

    print("should return 3")
    nums1 = [1, 3, 4]
    nums2 = [2, 5]
    print(findMedianSortedArrays(nums1, nums2))

    # Output:
    # Explanation: median is in the second list, even total length

    print("should return 0")
    nums1 = [0, 0, 0, 0, 0]
    nums2 = [-1, 0, 0, 0, 0, 0, 1]
    print(findMedianSortedArrays(nums1, nums2))

    print("should return 2")
    nums1 = [1,3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))
