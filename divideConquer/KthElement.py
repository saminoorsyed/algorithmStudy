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
