# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: optional[ListNode], n: int) -> optional[ListNode]:
    # start both pointers from the beginning
    left = right = head
    
    # increment the fast pointer as many times as n
    for i in range(n):
        right = right.next
    if not right.next:
        return left.next

    # move both pointers until right is pointing at the last node
    while right.next:
        right = right.next
        left = left.next

    # remove the indicated node from the linked list
    left.next = left.next.next
    
    return head

# functions to help test
def buildLinkedList(targetList):
    returnList = ListNode()
    pointer = returnList
    for index, value in enumerate(targetList):
        pointer.val = value
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
    # build list for re-ordering
    list1 = buildLinkedList([1,2, 3, 4])
    answer1 = removeNthFromEnd(list1, n)
    printLinkedList(answer1)
    
            