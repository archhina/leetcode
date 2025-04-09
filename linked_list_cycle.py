# 141. Linked List Cycle

def hasCycle(self, head: Optional[ListNode]) -> bool:

    seen = set()

    pointer = head

    while pointer:
        if pointer in seen:
            return True
        seen.add(pointer)
        pointer = pointer.next
    return False