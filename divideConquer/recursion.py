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


if __name__ == '__main__':
  a = [1,3,4,5,6,7,8,9]
  result = search(a, 9)
  print(result)
  arr = [1,2,12,22,96,105,600]
  result = search(arr, 12)
  print(result)