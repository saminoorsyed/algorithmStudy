# Sami Noor Syed
# ​ONID: ​​934330738
# Cs 325 Summer 2022
# Assignment 2
# due date: July 5th, 2022


def kthElement(arr1: list, arr2: list, k: int) -> int:
    """
    Function that finds the kth element of two sorted arrays when they are combined
    
    This solution is based on the following observations:
    
    Loop invariant: the kth element must be contained within array1[0: point1] and array2[0: point2] if the following are true
            point1+point2 = k 
            array1[point1] !> array2[point2+1]
            array2[point2] !> array1[point2+1].
    
    Divide:We can cut the arrays in half while adjusting k until array1[point1] < array2[point2+1] and array2[point2] < array1[point1+1]. 
    
    Conquer: Once we know that our k selection of points contains only the values <= the kth element according to the paradigm above, we can decide which element is our kth element based on the circumstances the arrays in question


    param: arr1: list, arr2: list, k: int
    return: int
    """
    n = len(arr1)
    m = len(arr2)
    # conquer: solve the sub-problems with all of the base cases
    if n ==1 or m == 1:
        #Make arr 1 the array with only one element and n = 1
        if m == 1:
            place_holder = arr1
            arr1 = arr2
            arr2 = place_holder
            m = n
            n = 1
        if k == 1:
            #if k == 1, the smaller of the two element will be the kth element. the larger will be the k+1 element
            return min(arr1[0], arr2[0])
        if k == 2:
            # given that k == 2, the larger value of the arrays will be equal to the kth element
            return max(arr1[0], arr2[0])
        else:
            if arr2[k-1] <= arr1[0]:
                return arr2[k-1]#if k is greater than 2, then arr[k-1] will be the kth element arr1[0] will be the k+1 element
            else:
                return max(arr1[0], arr2[k-2]) #if arr1[0] is smaller, then the arr2[k-1] is the k+1 element and the kth element will be the larger of arr1[0] and arr2[k-2]
    # divide: break down the arrays into smaller more manageable sub parts
    middle1 = (n-1)//2
    middle2 = (m-1)//2
    if k > middle1+middle2+1:
        # We don’t need to consider elements smaller than the largest of the other array this if statement helps us reduce the elements we have to compare
        if arr1[middle2] >= arr2[middle2]:
        # reduce the size of the second array by half, removing smaller elements and adjusting k to match
            return kthElement(arr1, arr2[middle2+1:], k - middle2 -1)
        else:
            #reduce the size of the first array by half, removing smaller elements and adjusting k to match
            return kthElement(arr1[middle1+1:], arr2, k - middle1 - 1)
    else: # k is smaller or equal to the number elements contained in the first halves.
        if arr1[middle2]>= arr2[middle2]:
            # reduce the size of the first array by half
            return kthElement(arr1[:middle1+1], arr2, k)
        else:
            # reduce the size of the second array by half Return Def kthElement(arr1, arr2[:middle1+1], k)
            return kthElement(arr1, arr2[:middle2+1],k)

def kth_optimized(arr1: list, arr2: list, k: int) -> int:
    """
    optimized version of the kth element algorithm. instead of dividing the entire array by 2, we adjust a marker on both the first and second arrays. the elements contained between arr1[0:l] and arr2[0:m] represent all and no more than k elements total.

    we can move this marker back and forth using a binary search like method (divide and conquer) to end on a valid placement for k in which arr1[l]< arr2[m+1] and arr2[l] < arr1[l+1]

    function returns the value of the kth element if the two sorted arrays, arr1 and arr2, are merged. this should be accomplished in log(k) time.

    Param: arr1: list, arr2: list, k: int;
    return: int
    """

    #make sure that the first array contains most of the points
    if len(arr2)> len(arr1):
        arr1, arr2 = arr2, arr1
    # initialize. Mark1 on the first array will be placed such that half of the k elements are on the first array. the rest of the elements should be contained in the second array.
    mark1 = k if k < len(arr1) else k-(k-len(arr1))-1
    print(mark1, arr1[mark1])
    mark2 = 0 if k < len(arr1) else k-mark1-2
    print(mark2)
    # if there are fewer elements in the array than k, the kth element does not exist in either array
    if len(arr1)+len(arr2) < k:
        return None
    
    if len(arr1)+len(arr2) == k:
        return max(arr1[-1], arr2[-1])
    
    if len(arr1)+len(arr2) == k+1:
        if arr1[mark1] <= arr2[mark2+1] or arr2[mark2] <= arr1[mark1+1]:
            return max(arr1[mark1], arr2[mark2])
        else:
            return max(arr1[mark1-1], arr2[mark2+1])

    while arr1[mark1] > arr2[mark2+1] or arr2[mark2] > arr1[mark1+1]:
        #adjust the placements of markers to include fewer elements on the array which contains the largest value (if that value is greater than the value stored in the other array's marker+1 value)
        print(mark1, mark2)
        if arr1[mark1]> arr2[mark2+1]:
            mark1 = (mark1-1)//2
            mark2 = k-mark1-2
            while len(arr2)
        elif arr2[mark2]> arr1[mark1+1]:
            mark2 = (mark2-1)//2
            mark1 = k-mark2-2
    
    return max(arr1[mark1], arr2[mark2])
