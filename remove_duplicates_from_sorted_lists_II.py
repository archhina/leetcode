# 82. Remove Duplicates from Sorted List II

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

    dummy = ListNode()
    dummy.next = head
    pointer = dummy

    while pointer:
        if pointer.next and pointer.next.next and pointer.next.val == pointer.next.next.val:
            tmp = pointer.next.next
            while tmp and tmp.next and tmp.val == tmp.next.val:
                tmp = tmp.next
            pointer.next = tmp.next
        else:
            pointer = pointer.next
        
    return dummy.next