# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:

    # determine which list is larger and make that list 1
    if len(nums1)>= len(nums2):
        list1, list2 = nums1, nums2
    else:
        list1, list2 = nums2, nums1
    # deal with edge cases first in which we don't need to mix the lists to find the median:

    # the case in which there is not a second list
    if len(list2) == 0:
        # the list is odd, we return the middle number
        if len(list1)%2 ==1:
            return list1[len(list1)//2]
        # the list is even, return the average of the two middle numbers
        else:
            return (list1[len(list1)//2]+list1[len(list1)//2-1])/2
    
    # figure out what index number element we are looking for
    totalLen = len(list1)+len(list2)
    median = (len(list1)+len(list2))//2
    # if the list is even, we need the average of the two middle numbers
    # the case in which all the elements of the shorter list are >= the elements of the longer list
    if list1[-1]<list2[0]:
        if median == len(list1):
            return (list1[-1]+list2[0])/2 if totalLen%2 ==0 else list1[-1]
        return (list1[median]+ list1[median-1])/2 if totalLen%2 ==0 else list1[median]

    # the case in which all the elements of the longer list are >= the elements of the shorter list
    if list2[-1]<list1[0]:
        if median == len(list1):
            return (list1[-1]+list2[0])/2 if totalLen%2 ==0 else list1[-1]
        median -= (len(list2))
        # there is an even number of elements
        return (list1[median]+list1[median-1])/2 if totalLen%2 ==0 else list1[median]
    if len(list1)==1 and len(list2) == 1:
        return (list1[0]+list2[0])/2
    # the case in which all the elements in one list are not greater than the elements in another list
    # starting from median element of the longer list -1, and the beginning of the shorter list we perform an adjustment using binary search
    # since we know the first list is longer, we know it has at least median elements in it
    high = median-1
    low = 0
    # since at least one value from each element must be included, we know that there is an element k in the first list that elements from 0->k in the first and from 0-> median-2 in the second contain the first half of the list
    while low< high:
        if list1[high]> list2[median-high]:
            high = (low+high)//2
        else:
            low = (low+high)//2+1
    
    if totalLen%2 ==1:
        return max(list1[high], list2[median-high-2])
    else:
        higher = max(list1[high],list2[median-high-1])
        if higher == list1[high]:
            if high==0:
                return (higher+list2[median-high-1])/2
            else:
                return (higher+max(list1[high-1],list2[median-high-1]))/2
        else:
            return (higher+max(list2[median-high-2],list1[high]))/2

        

    # while ((marker1+1< len(list1)) and list2[marker2]>list1[marker1+1]) or ((marker2+1 <len(list2)) and list1[marker1] > list2[marker2+1]):
    #     if (marker1+1< len(list1)) and list2[marker2]>list1[marker1+1]:
    #         adjustment = marker2//2 - 1
    #         marker2 -= adjustment
    #         marker1 = median-2 - marker2
    #     else:
    #         adjustment = marker1//2
    #         marker1 -= adjustment
    #         marker2 = median-2 -marker1
    # if totalLen%2 ==1:
    #     return max(list1[marker1], list2[marker2])
    # else:
    #     higher = max(list1[marker1],list2[marker2])
    #     if higher == list1[marker1]:
    #         return (higher+max(list1[marker1-1],list2[marker2]))/2
    #     else:
    #         return (higher+max(list2[marker2-1],list1[marker1]))/2


    # depending on which element is larger, return the median 

if __name__ == "__main__":
    # Example 1:

    nums1 = [1,2,3,4,5,6,7]
    nums2 = []

    print(findMedianSortedArrays(nums1,nums2))
    # Output: 4
    # Example 2:

    nums1 = []
    nums2 = [1,2,3,4,5,6,7]
    print(findMedianSortedArrays(nums1,nums2))

    # Output: 4
    # Explanation: same as the last test, checking that longer list is assigned list 1 in code

    nums1 = [8,9,10]
    nums2 = [1,2,3,4,5,6,7]
    print(findMedianSortedArrays(nums1,nums2))

    # Output: 5.5
    # Explanation: check that median is average of 6 and 7

    nums1 = [8,9,10]
    nums2 = [1,2,3]
    print(findMedianSortedArrays(nums1,nums2))

    # Output: 5.5
    # Explanation: median is the average of 3 and 8

    nums1 = [7,8,9,10]
    nums2 = [1,2,3]
    print(findMedianSortedArrays(nums1,nums2))

    # Output: 7
    # Explanation: median is in the second list, odd total length

    nums1 = [6,7,8,9,10]
    nums2 = [1,2,3]
    print(findMedianSortedArrays(nums1,nums2))

    # Output: 6.5
    # Explanation: median is in the second list, even total length

    nums1 = [1,3]
    nums2 = [2,7]
    print(findMedianSortedArrays(nums1,nums2))

    # Output: 2.5
    # Explanation: median is in the second list, even total length

    nums1 = [0,0]
    nums2 = [0,0]
    print(findMedianSortedArrays(nums1,nums2))

    # Output:
    # Explanation: median is in the second list, even total length

    nums1 = [1,2]
    nums2 = [1,1]
    print(findMedianSortedArrays(nums1,nums2))

    # Output:
    # Explanation: median is in the second list, even total length
    
    nums1 = [1,3,4]
    nums2 = [2,5]
    print(findMedianSortedArrays(nums1,nums2))

    # Output:
    # Explanation: median is in the second list, even total length