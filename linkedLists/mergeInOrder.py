class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # create an empty list
    mergedList = ListNode()
    pointer = mergedList
    # loop through each list, advancing the pointer and building the merged list
    while list1 and list2:
        pointer.next = ListNode()
        pointer = pointer.next
        if list1.val <= list2.val:
            pointer.val = list1.val
            list1 = list1.next
        else:
            pointer.val = list2.val
            list2 = list2.next

    if list1:
        pointer.next = list1
    else:
        pointer.next = list2
    return mergedList.next

def buildLinkedList(targetList):
    returnList = ListNode()
    pointer = returnList
    for index, val in enumerate(targetList):
        pointer.val = val
        if index<len(list1)-1:
            pointer.next = ListNode()
            pointer = pointer.next
    return returnList

def printLinkedList(head):
    while head:
        print(head.val)
        head = head.next
    return None

if __name__ == "__main__":
    list1 = [1,3,5]
    list2 = [2,4,6]
    link1 = buildLinkedList(list1)
    link2 = buildLinkedList(list2)

    mergedList = mergeTwoLists(link1, link2)
    printLinkedList(mergedList)
    