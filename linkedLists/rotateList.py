def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    end_node = iter_node = head
    count = 0
    while iter_node:
        end_node = iter_node
        count+=1
        iter_node = iter_node.next
    if head == end_node or k == 0:
        return head
    k = count - (k % count)
    end_node.next = head
    while k:
        end_node = end_node.next
        head = head.next
        k -=1
    end_node.next = None
    return head
