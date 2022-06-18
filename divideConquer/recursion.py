
def divide_search(arr: list, target: int, start: int = 0, end : int = -1,) -> int:
    '''
    Search for an element in a list of sorted numbers using Divide and Conquer Technique. If the element is found return the index of the key, else return -1.

    Function definition: search(numList, key)
    sample input: numList = [1,3,4,5,6,7,8,9]; key=9
    output: 7
    '''
    if end == -1:
        end = len(arr)

    if start < end:
        middle = (start + end) // 2
        divide_search(arr, target, start, middle)
        divide_search(arr, target, middle+1, end)
    if arr[start] == target:
        return start
    else:
        return -1

