# sort a linked list in O(nlogn) time and in O(1) space complexity

# thought process, use merge sort and do it piece by piece. find the middle node, split the list recursively and then merge them in sorted order


def sortList(head, count:int = 1):
    if not head or not head.next:
        return head

    def findMid(head):
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeInOrder(left, right):
        placeH = ListNode(0)
        current = placeH

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        if left:
            current.next = left
        if right:
            current.next = right

        return placeH.next
    # split the lists into two distinct halves
    middle = findMid(head)
    leftSide = head
    rightSide = middle.next
    middle.next = None

    leftSorted = sortList(leftSide)
    rightSorted = sortList(rightSide)

    mergedList = mergeInOrder(leftSorted, rightSorted)

    return mergedList
