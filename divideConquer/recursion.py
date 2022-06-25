def binary_search(arr, start, end, target):
    if start <= end:
        middle = (start + end) // 2
        print(start,middle, end)
        if arr[middle] == target:
            # found
            return middle

        if arr[middle] > target:
            return binary_search (arr, start, middle-1, target)

        if arr[middle] < target:
            return binary_search(arr, middle+1, end, target)
    # not found
    return -1  


def search(arr, key):
    return binary_search(arr, 0, len(arr)-1, key)



def kthElement(arr1: list, arr2: list, k: int):
    """
    Function that finds the kth element of two sorted arrays when they are combined
    This solution is based on the fact that the kth element must be contained within
    array1[0: point1] and array2[0: point2] if point1+point2 = k. We can cut the arrays in half
    until array1[point1] < array2[point2+1] and array2[point2] < array1[point1+1]
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
            return min(arr1[0], arr2[0])
        if k == 2:
            return maximum(arr[0], arr2[0])
        else: #if k is greater than 2
            if arr2[k-1] < arr[0]:
                return arr2[k-1] #this is the kth element
            else:
                return max(arr[0],arr2[k-2]) #the kth is the larger of the two
    #divide/ break down the arrays into smaller more manageable sub parts
    middle1 = (n-1)//2
    middle2 = (m-1)//2
    if k > middle1+middle2+1:
    # we don’t need to consider elements smaller than the largest of the other array, adjust k and arrays accordingly
        if arr1[middle2]> arr2[middle2]:
        # reduce the size of the second array by half
            return kthElement(arr1, arr2[middle2+1:], k - middle2 -1)
        else:
            #reduce the size of the first array by half
            return kthElement(arr1[middle1+1:], arr2, k - middle1 - 1)
    else: # k is smaller or equal to the number elements contained in the first halves.
        if arr1[middle2]> arr2[middle2]:
            # reduce the size of the first array by half
            return kthElement(arr1[:middle1+1], arr2, k)
        else:
            # reduce the size of the second array by halfReturn Def kthElement(arr1, arr2[:middle1+1], k)
            return kthElement(arr1, arr2[:middle2],k)

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



if __name__ == '__main__':
    
    arr1 = [-5,1,2,2,3,5,6]
    arr2= [-7,3,4,5,6,7]
    k= 5

    # print(kthElement(arr1, arr2, 5))

    arr1 = [-5,1,2,2]
    arr2= [-7,3,4]
    k= 4

    print(kth_optimized(arr1, arr2, 5))