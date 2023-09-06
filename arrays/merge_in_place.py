def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        for index in range(m):
            if i<m and nums1[i]<nums2[j] and nums1[i]!= 0:
                i+=1
            else:
                nums1.insert(i, nums2[j])
                i +=1
                j +=1
                nums1.pop()


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)
