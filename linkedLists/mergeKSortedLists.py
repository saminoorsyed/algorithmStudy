"""You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []"""

# Brute force is to iterate through each list in a row and add it to a master list. if all lists are of n size, then each merge operation will use the following number of operation n, 2n, 3n, 4n, 5n
# instead, we should aim to merge lists of equal lengths. so that we get a solution more akin to the merge sort algo. here we pop and then merge the first two items in the list, and add the result to the back of the list. we continue this process until only one Item remains
# in this way, equal length lists are always merged

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        def mergeList(l1, l2):
            cur = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next

            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return dummy.next

        while len(lists)>=2:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            lists.append(mergeList(l1, l2))

        return lists[0]