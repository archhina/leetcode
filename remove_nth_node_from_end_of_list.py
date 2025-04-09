# 19. Remove Nth Node From End of List

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    length = 0
    l1 = head

    while l1:
        l1 = l1.next
        length += 1
    
    if length == 1:
        return None
    l1 = head
    if n == 1:
        for i in range(length-n-1):
            l1 = l1.next
        l1.next = None
    else:
        for i in range(length-n):
            l1 = l1.next
        l2 = l1
        l2 = l2.next
        l1.val = l2.val
        l1.next = l2.next
    
    return head