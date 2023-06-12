# problem statement:
# You are given the head of a singly linked-list. The list can be represented as:
# 
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def splitList(head: ListNode) -> (ListNode, ListNode):
    # split the list
    incrementBy1 = head
    incrementBy2 = head.next
    # one iteration in O(n) time
    while incrementBy2 and incrementBy2.next:
        incrementBy1 = incrementBy1.next
        incrementBy2 = incrementBy2.next.next
    middle = incrementBy1.next
    incrementBy1.next = None
    return head, middle

def reverseListInPlace(head: ListNode)-> ListNode:
    """ Reverses a linked list in place"""
    lastNode = None
    currentNode = head
    while currentNode:
        nextNode = currentNode.next #increment next node
        currentNode.next = lastNode #point the current node at the last node
        lastNode = currentNode      #make the last node the new current node
        currentNode = nextNode      #make the current node the next node in the original list
    return lastNode

# this solution runs in O(n) time
def reorderList(head: ListNode) -> None:
    # split the list
    firstHalf, secondHalf = splitList(head)
    # reverse the order of the second list in place by switching the direction of pointers
    reversedSecondHalf = reverseListInPlace(secondHalf)
    head = firstHalf
    firstHalf = firstHalf.next
    # if the number of nodes is even, the loop should run out of first half before second half
    while head:
        if reversedSecondHalf:
            head.next = reversedSecondHalf
            reversedSecondHalf = reversedSecondHalf.next
            head = head.next
        if firstHalf:
            head.next = firstHalf
            firstHalf = firstHalf.next
            head = head.next
        if not firstHalf and not reversedSecondHalf:
            head = head.next

# # this solution runs in )(n^2) time
# def reorderList(head: ListNode) -> None:
#     """
#     Do not return anything, modify head in-place instead.
#     """
#     # since we have to modify everything in place, this solution will require that we  use pointers to keep track of each node
#     # the first pointer should keep track of the first element of the intact list
#     intactPointer = head
#     while intactPointer:
#         # we also need to point to the last item in the intact list
#         lastPointer = intactPointer
#         while lastPointer.next:
#             secondToLast = lastPointer
#             lastPointer = lastPointer.next
#             if lastPointer.next == None:
#                 secondToLast.next = None             
#         intactPointer = intactPointer.next
#         head.next = lastPointer
#         head = head.next
#         head.next = intactPointer
#         head = head.next
        

# functions to help test
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
    # build list for re-ordering
    list1 = [1,2]
    link1 = buildLinkedList(list1)
    # reorder list
    reorderList(link1)
    printLinkedList(link1)
    